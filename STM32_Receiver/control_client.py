import os
import socket
import subprocess
import sys
import json
from typing import Dict

from STM32_Receiver.udp_tool import CONTROL_CODE_MAP, UDPTool


CONTROL_PROCESS_TIMEOUT = float(os.getenv("UDP_CONTROL_PROCESS_TIMEOUT", "10"))


def _worker_script_path() -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "control_worker.py")


def send_udp_control_command(turbine_id: str, data_type: int, control_key: str, value: int) -> Dict[str, str]:
    normalized_key = control_key.upper()
    if normalized_key not in CONTROL_CODE_MAP:
        raise ValueError(f"不支持的控制对象: {control_key}")

    command = [
        sys.executable,
        _worker_script_path(),
        turbine_id,
        str(data_type),
        normalized_key,
        str(value),
    ]

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=CONTROL_PROCESS_TIMEOUT,
            check=False,
        )
    except subprocess.TimeoutExpired:
        raise socket.timeout("等待目标地址响应超时")

    stdout_text = (completed.stdout or "").strip()
    stderr_text = (completed.stderr or "").strip()

    if not stdout_text:
        raise OSError(stderr_text or f"控制进程异常退出，退出码: {completed.returncode}")

    try:
        payload = json.loads(stdout_text)
    except json.JSONDecodeError as exc:
        raise OSError(f"控制进程输出无法解析: {stdout_text}") from exc

    if payload.get("ok"):
        return payload["result"]

    error_type = str(payload.get("error_type", ""))
    error_message = str(payload.get("error_message", "未知错误"))
    if error_type.lower() in {"timeout", "socket.timeout"} or error_type == "TimeoutError":
        raise socket.timeout(error_message)
    if error_type == "ValueError":
        raise ValueError(error_message)
    raise OSError(error_message)
