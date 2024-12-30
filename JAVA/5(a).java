import java.util.*;
interface isro
{
void input();
void result(int x);
}
class Pair implements isro
{
String state [] = new String [10];
String name [] = new String [10];
public int n;
Scanner sc = new Scanner(System.in);
public void result(int n)
{
int count=0;
for(int i=1;i<=n;i++)
{
for(int j=i;j<=n;j++)
{
if(i!=j)
{
if(state[i].equalsIgnoreCase(state[j])==false)
{
count++;
System.out.println("The possible pair:"+count+"\t=\t["+name[i]+"] from state
["+state[i]+"] and ["+name[j]+"] from state ["+state[j]+"]");
}
}
}
}
System.out.println("A total of "+count+" possibilities of pairs from different states were
detected.");
}
public void input()
{
System.out.println("Enter the no of astronauts:");
n=sc.nextInt();
System.out.println("Enter the state details now:");
for(int i=1;i<=n;i++)
{
System.out.println("Enter name of Astronaut: "+i);
name[i]=sc.next();
System.out.println("Enter state of Astronaut: "+i);
state[i]=sc.next();
System.out.println();
}
}
} class demo
{
public static void main(String[]args)
{
Pair B = new Pair();
Scanner sc = new Scanner(System.in);
int y;
do
{
B.input();
B.result(B.n);
System.out.println("Do you wish to repeat? (Press 0)");
y=sc.nextInt();
}while(y==0);
}
}
