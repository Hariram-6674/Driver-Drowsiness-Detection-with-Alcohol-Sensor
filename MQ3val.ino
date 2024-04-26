// Define the analog pin connected to the MQ3 sensor
const int mq3Pin = A0;

void setup() {
 // Start serial communication at 9600 baud rate
 Serial.begin(9600);
}

void loop() {
 // Read the analog value from the MQ3 sensor
 int mq3Value = analogRead(mq3Pin);

 // Send the value to the Raspberry Pi
 Serial.println(mq3Value);

 // Wait for a short period before the next reading
 delay(1000);
}
