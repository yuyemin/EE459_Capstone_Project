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
void setSprinklerZones(int sprinklerZoneCount, int sprinklerZones[4]);
void initSprinklerZones(int sprinklerZoneCount, int sprinklerZones[4]);

// ****
// MAIN
// ****

int main(void)
{
    // sets all our IO bits
    DDRC |= 1 << DDC0;          // Set PORTC bit 0 for output
    


    // sets up communication with raspberry pi IN PROGRESS
    const int sprinklerZoneCount = 4;
    int sprinklerZones[sprinklerZoneCount];
    initSprinklerZones(sprinklerZoneCount, sprinklerZones);

    //forever loop
    while (1) {
        
        // reads through all of the sprinkler zones and sets them to their value
        setSprinklerZones(sprinklerZoneCount, sprinklerZones);
        _delay_ms(10); // delays for 10ms between iterations
        
    }

    return 0;   /* never reached */
}

// *********
// FUNCTIONS
// *********

void initSprinklerZones(int sprinklerZoneCount, int sprinklerZones[4]) {
    //initializes all PC0-3 for output
    DDRC |= 1 << DDC0;          // Set PORTC bit 0 for output
    DDRC |= 1 << DDC1;  
    DDRC |= 1 << DDC2;
    DDRC |= 1 << DDC3;        
    // defaults all the sprinkler zones to OFF
    int i = 0;
    for (i = 0; i < sprinklerZoneCount; i++) {
        sprinklerZones[i] = 0;
    }
}

// sets all the sprinkler zones using the sprinklerZones[] integer array and ports PC0-3
void setSprinklerZones(int sprinklerZoneCount, int sprinklerZones[4]) {
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
}