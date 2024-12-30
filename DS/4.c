#include <stdio.h>
#include<stdlib.h>
#define CAPACITY 20
void insert();
void delete();
void display();
int queue_array[CAPACITY];
int rear = - 1;
int front = - 1;
void main()
{
int choice;
while (1)
{
printf("\n1.Enter 1 to insert element to queue \n");
printf("2.Enter 2 to delete element from queue \n");
printf("3.Enter 3 to display all elements of queue \n");
printf("4.Enter 4 to quit \n");
printf("Enter your choice : ");
scanf("%d", &choice);
switch (choice)
{
case 1: insert();
break;
case 2: delete();
break;
case 3: display();
break;
case 4: exit(0);
default:printf("Wrong choice \n");
}
}
}
void insert()
{
int element;
21CSL35:Data Structures Laboratory
12
Department of Computer Science & Engineering, SCEM, Mangaluru.
if (rear == CAPACITY - 1)
printf("Queue is full\n");
else
{
if (front == - 1)
front = 0;
printf("Enter element which is to be inserted ");
scanf("%d", &element);
rear = rear + 1;
queue_array[rear] = element;
}
} /* End of insert() */
void delete()
{
if (front == - 1 || front > rear)
{
printf("Queue is empty we cannot delete an element \n");
return ;
}
else
{
printf("Element deleted from queue is : %d\n", queue_array[front]);
front = front + 1;
}
} /* End of delete() */
void display()
{
int i;
if (front==-1 || front > rear)
printf("Queue is empty \n");
else
{
printf("Elements of Queue are: \n");
for (i = front; i <= rear; i++)
printf("%d\t", queue_array[i]);
printf("\n");
printf("***********************\n");
printf("Categorization of data\n");
printf("***********************\n");
printf("Group 1: Less than 10\n");
for(i=front;i<=rear;i++)
{
if(queue_array[i]<10)
{
printf("%d\t",queue_array[i]);
}
}
printf("\nGroup 2: Between 10 & 19\n");
for(i=front;i<=rear;i++)
{
if(queue_array[i]>=10 && queue_array[i]<=19)
{
printf("%d\t",queue_array[i]);
}
}
printf("\nGroup 3: Between 20 & 29\n");
for(i=front;i<=rear;i++)
{
if(queue_array[i]>=20 && queue_array[i]<=29)
{
printf("%d\t",queue_array[i]);
}
}
printf("\nGroup 4: 30 & greater\n");
for(i=front;i<=rear;i++)
{
if(queue_array[i]>=30)
{
printf("%d\t",queue_array[i]);
}
}
}
}
