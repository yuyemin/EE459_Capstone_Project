/*
at328.c
Atmega328p Code
EE459 Final Project

CB: Michael Kukar


*/

#include <avr/io.h>
#include <util/delay.h>

// ********************
// PREDEFINED FUNCTIONS
// ********************
void getZonesFromSerial(int sprinklerZoneCount, int sprinklerZones[4], unsigned char confirmationChar);
void setSprinklerZones(int sprinklerZoneCount, int sprinklerZones[4]);
void initSprinklerZones(int sprinklerZoneCount, int sprinklerZones[4]);
void usart_init(unsigned short);
void usart_out(char);
char usart_in();


// ****
// MAIN
// ****

int main(void)
{
    // sets all our IO bits
    

    // sets up communication with raspberry pi over serial
    usart_init(47);
    
    
    const int sprinklerZoneCount = 6;
    int sprinklerZones[sprinklerZoneCount];
    initSprinklerZones(sprinklerZoneCount, sprinklerZones);

    //initializes sprinkler zones to 0
    setSprinklerZones(sprinklerZoneCount, sprinklerZones);
    _delay_ms(10);

    // SERIAL VARIABLES
    unsigned char zoneUpdate = 122; //'z'  if we get this, we know to update the zones
    unsigned char confirmationChar = 97; //'a'  sends this back on good data received

    //forever loop
    while (1) {
        
        // checks for a serial value to come across that corresponds to the zones to be on
        
        unsigned char rawInput = usart_in();
        if (rawInput == zoneUpdate) {
        
            getZonesFromSerial(sprinklerZoneCount, sprinklerZones, confirmationChar);
            setSprinklerZones(sprinklerZoneCount, sprinklerZones);
        }
        
        
        _delay_ms(10); // delays for 10ms between iterations
        
    }

    return 0;   /* never reached */
}

// *********
// FUNCTIONS
// *********

// gets the serial zones and then updates the sprinklerZones array
void getZonesFromSerial(int sprinklerZoneCount, int sprinklerZones[6], unsigned char confirmationChar) {
    int i = 0;
    for (i = 0; i < sprinklerZoneCount; i++) {
        unsigned char rawIn = usart_in();
        if (rawIn == 48) { //0
            sprinklerZones[i] = 0;
        }
        else if (rawIn == 49) { //1
            sprinklerZones[i] = 1;
        }
        // otherwise doesn't modify the value
        
    }
    // prints out a confirmation that it sent correctly
    usart_out(confirmationChar);
}


void initSprinklerZones(int sprinklerZoneCount, int sprinklerZones[6]) {
    //initializes all PC0-5 for output
    DDRC |= 1 << DDC0;          // Set PORTC bit 0 for output
    DDRC |= 1 << DDC1;  
    DDRC |= 1 << DDC2;
    DDRC |= 1 << DDC3;   
    DDRB |= 1 << DDB2;
    DDRB |= 1 << DDB1;
         
    // defaults all the sprinkler zones to OFF
    int i = 0;
    for (i = 0; i < sprinklerZoneCount; i++) {
        sprinklerZones[i] = 0;
    }
}

// sets all the sprinkler zones using the sprinklerZones[] integer array and ports PC0-3
void setSprinklerZones(int sprinklerZoneCount, int sprinklerZones[6]) {
    if (sprinklerZones[0] == 0) {
        PORTC &= ~(1 << PC0);      // Set PC0 to a 0
    }
    else {
        PORTC |= 1 << PC0;      // Set PC0 to a 1
    }
    
    if (sprinklerZones[1] == 0) {
        PORTC &= ~(1 << PC1);      // Set PC0 to a 0
    }
    else {
        PORTC |= 1 << PC1;      // Set PC0 to a 1
    }
    
    if (sprinklerZones[2] == 0) {
        PORTC &= ~(1 << PC2);      // Set PC0 to a 0
    }
    else {
        PORTC |= 1 << PC2;      // Set PC0 to a 1
    }
    
    if (sprinklerZones[3] == 0) {
        PORTC &= ~(1 << PC3);      // Set PC0 to a 0
    }
    else {
        PORTC |= 1 << PC3;      // Set PC0 to a 1
    }
    
    if (sprinklerZones[4] == 0) {
        PORTB &= ~(1 << PB2);      // Set PC0 to a 0
    }
    else {
        PORTB |= 1 << PB2;      // Set PC0 to a 1
    }
    
    if (sprinklerZones[5] == 0) {
        PORTB &= ~(1 << PB1);      // Set PC0 to a 0
    }
    else {
        PORTB |= 1 << PB1;      // Set PC0 to a 1
    }
}

// SERIAL COMMANDS
/*
usart_init - Initialize the USART port
*/
// SET THIS TO 47 for 9600 BAUD RATE
void usart_init(unsigned short ubrr) {
    UBRR0 = ubrr;
    UCSR0B |= (1 << TXEN0);
    UCSR0B |= (1 << RXEN0);
    UCSR0C = (3 << UCSZ00);
}

// usart_out - Output a byte

void usart_out(char ch) {
    while ((UCSR0A & (1<<UDRE0)) == 0);
    UDR0 = ch; 
}

/*
usart_in - Read a byte from the USART0 and return it
*/ 
char usart_in() {
    while ( !(UCSR0A & (1 << RXC0)) );
    return UDR0;
}