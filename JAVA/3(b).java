class Vehicle
{
String vehicle_id;
int fuel_cap;
int fuel_cons_rate;
Vehicle(String vid, int fc, int fcr)
{
vehicle_id=vid;
fuel_cap=fc;
fuel_cons_rate=fcr;
}
void display()
{
System.out.println("");
System.out.print("vehicle_id\tfuel_cap\tfuel_cons_rate");
System.out.print("\n----------------------------------------------------------------------");
System.out.print("\n");
System.out.println(vehicle_id+"\t\t"+fuel_cap+"\t\t"+fuel_cons_rate);
}}
class Bus extends Vehicle
{ int seating_cap;
Bus(String vid, int fc, int fcr,int ss)
{s
uper(vid,fc,fcr);
seating_cap=ss;
}
void display()
{
System.out.println(".........Bus Information.............");
super.display();
System.out.println("Seating capacity");
System.out.println(seating_cap+"\t");
}}
class Truck extends Vehicle
{ int carrying_cap;
Truck(String vid, int fc, int fcr,int cc)
{s
uper(vid,fc,fcr);
carrying_cap=cc;
}
void display()
{
System.out.println("..........Truck Information............");
super.display();
System.out.println("Carrying capacity");
System.out.println("\t"+carrying_cap);
}}
class Assign3b
{
public static void main(String args[])
{
Bus b=new Bus("1234",60,25,50);
Truck t=new Truck("1236",50,20,40);
b.display();
t.display();
}}
