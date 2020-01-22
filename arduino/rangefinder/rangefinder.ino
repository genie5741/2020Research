const int trigPin = 13;
const int echoPin = 12;

long duration;
int distance;
String temp;
bool flag;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //Start The Monitor Serial 
  Serial.begin(9600);
}

int get_distance(){
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration*0.034/2; //cm
  return distance;
}


void loop() {
  if(Serial.available()){
    temp = Serial.readStringUntil('\n');
    if (temp == "on") flag = 1;  //ascii 49 = 1
    else if (temp == "off") flag = 0;  //ascii 48 = 0
  }

  if(flag) Serial.println(get_distance()); //unit: cm
}
