#include <avr/io.h>
#include <util/delay.h>
#include <math.h>
#include <stdlib.h>

#define F_CPU 8000000L

#define LED        PB1
#define LED_PORT   PORTB
#define THERM      PB0
#define THERM_PORT PORTB

void read_therm()
{
  DDRB |= 1<<THERM;
  THERM_PORT &= ~(1<<THERM);
  _delay_ms(5);
  LED_PORT |= 1<<LED;
  DDRB &= ~(1<<THERM);
  THERM_PORT &= ~(1<<LED);
  
  While(i!=40)
  {
    _delay_us(22);
    currentHumidity    = 0;
    currentTemperature = 0;
    checkSum           = 0;
    // First 16 bits is Humidity
    for (i=0; i<16; i++) {
        //printf("bit %d: %d  ", i, bitTimes[i+1]);
        if (bitTimes[i+1] > 0) {
            currentHumidity |= ( 1 << (15-i));
        }
    }
    
    // Second 16 bits is Temperature 
    for (i=16; i<32; i ++) {
        //printf("bit %d: %d  ", i, bitTimes[i+1]);
        if (bitTimes[i+1] > 0) {
            currentTemperature |= (1 <<(31-i));
        }
    }
 
    // Last 8 bit is Checksum
    for (i=32; i<40; i++) {
        //printf("bit %d: %d  ", i, bitTimes[i+1]);
        if (bitTimes[i+1] > 0) {
            checkSum |= (1 << (39-i));
        }
    }
   
    _lastHumidity = (float(currentHumidity) / 10.0);
    
    // if first bit of currentTemperature is 1, it is negative value.
    if ((currentTemperature & 0x8000)==0x8000) {        
        _lastTemperature = (float(currentTemperature & 0x7FFF) / 10.0) * -1.0;
    } else {
        _lastTemperature = float(currentTemperature) / 10.0;
    }
  }
  
}
  
