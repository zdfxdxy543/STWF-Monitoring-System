import contextlib
import io
import json
import sys

from udp_tool import UDPTool


def main() -> int:
	if len(sys.argv) != 5:
		print(json.dumps({
			"ok": False,
			"error_type": "ValueError",
			"error_message": "参数数量错误"
		}, ensure_ascii=False))
		return 2

	turbine_id = sys.argv[1]
	data_type = int(sys.argv[2])
	control_key = sys.argv[3]
	value = int(sys.argv[4])

	try:
		with contextlib.redirect_stdout(io.StringIO()):
			result = UDPTool.send_control_command(
				turbine_id=turbine_id,
				data_type=data_type,
				control_key=control_key,
				value=value,
			)
		print(json.dumps({"ok": True, "result": result}, ensure_ascii=False))
		return 0
	except Exception as exc:
		print(json.dumps({
			"ok": False,
			"error_type": exc.__class__.__name__,
			"error_message": str(exc),
		}, ensure_ascii=False))
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
