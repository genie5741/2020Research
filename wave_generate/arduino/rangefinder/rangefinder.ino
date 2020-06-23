// should return time also. should be modified


const int trigPin = 13;
const int echoPin = 12;

long duration;
int distance;
char temp;
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
  if(Serial.available()) {
    temp = Serial.read();
    if (temp == '1') flag = 1;
    else if (temp == '0') flag = 0;
  }

  if(flag) Serial.println(get_distance()); //unit: cm
}
