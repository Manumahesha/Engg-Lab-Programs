#include<stdio.h>
#include<string.h>
void findPaths(int m[50][50],int row,int col,int n);
int visited[50][50],count=0;
void main()
{
int n,a[50][50],row,col;
printf("enter the size of maze:");
scanf("%d",&n);
printf("enter the maze values in the form of 1's & 0's:(1->open; 0->close)\n");
for (int i = 0; i < n; i++)
for (int j = 0; j < n; j++)
scanf("%d",&a[i][j]);
printf("enter the entrance spot (i.e row value, column value):");
scanf("%d%d",&row,&col);
if(a[row][col]==0)
{
printf("No path found\n");
return;
}
findPaths(a,row,col,n);
if(count==0)
{
printf("No path found\n");
return;
}
}
void findPaths(int m[50][50],int row,int col,int n)
{
if(row==n-1 && col==n-1)
21CSL35:Data Structures Laboratory
4
Department of Computer Science & Engineering, SCEM, Mangaluru.
{
count++;
visited[row][col]=1;
printf("\nSolution %d:\n",count);
for (int i = 0; i < n; i++)
{
for (int j = 0; j < n; j++)
printf("%d ",visited[i][j]);
printf("\n");
}
visited[row][col]=0;
return;
}
else
{
visited[row][col]=1;
}
if(row+1<n && visited[row+1][col]==0 && m[row+1][col]==1)
{
findPaths(m,row+1,col,n); //DOWN
}
if(col-1>=0 && visited[row][col-1]==0 && m[row][col-1]==1)
{
findPaths(m,row,col-1,n); //LEFT
}
if(col+1<n && visited[row][col+1]==0 && m[row][col+1]==1)
{
findPaths(m,row,col+1,n); //RIGHT
}
if(row-1>=0 && visited[row-1][col]==0 && m[row-1][col]==1)
{
findPaths(m,row-1,col,n); //UP
}
visited[row][col]=0;
}
