#include "main.h"
#include "atk_mo395q.h"
#include "usart.h"
#include "adc.h"
#include "tim.h"
#include "stm32f1xx_it.h"

#define SOCKET_PROTO ATK_MO395Q_SOCKET_UDP
#define SOCKET_DES_IP_1  192
#define SOCKET_DES_IP_2  168
#define SOCKET_DES_IP_3  1
#define SOCKET_DES_IP_4  2
#define SOCKET_DES_PORT  8080
#define SOCKET_SOUR_PORT 8081

#define SEND_DATA 0xFF
#define ASK       0x00
#define OUT1      0x01
#define OUT2      0x02
#define OUT3      0x03
#define PWM1      0x04
#define PWM2      0x05

void system_init(void);
void system_run(void);
void Deal_Recv(uint8_t *buf);
void TIM1_Update_Interrupt_Enable(void);
void TIM1_Update_Interrupt_Disable(void);