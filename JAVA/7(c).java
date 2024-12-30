import java.util.Scanner;
public class Assign7c {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
// input instances
double num1, num2;
// reading input
System.out.print("Enter first number: ");
num1 = sc.nextDouble();
System.out.print("Enter second number: ");
num2 = sc.nextDouble();
// try-catch block for arithmetic exception
try {
if(num2==0)
throw new ArithmeticException("Devide by 0 error");
result = num1 / num2;
System.out.println("Result: " + result);
}
catch (ArithmeticException e)
{
System.out.println("Error: Cannot divide by zero.");
}
// input instances
int size;
int[] arr;
// reading input
System.out.print("Enter size of array: ");
size = sc.nextInt();
arr = new int[size];
System.out.println("Enter elements of array: ");
for (int i = 0; i < size; i++) {
arr[i] = sc.nextInt();
}
// try-catch block for array out of bounds exception
try {
int index;
System.out.print("Enter index to access: ");
index = sc.nextInt();
System.out.println("Element at index " + index + ": " + arr[index]);
} catch (ArrayIndexOutOfBoundsException e) {
System.out.println("Error: Invalid index.");
}
}
}
