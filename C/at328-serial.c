

#include <avr/io.h>
#include <util/delay.h>

void usart_init(unsigned short);
void usart_out(char);
char usart_in();

int main(void) {

    usart_init(47);
    
    while(1) {
        usart_out(usart_in() - 1);
    }
    
    return 0;
}

/*
usart_init - Initialize the USART port
*/
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