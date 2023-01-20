#include <stdio.h>
void main()
{
    printf("NON PREEMPTIVE PROCESS SCHEDULING\n");
    int n;
    printf("Enter the number of processes: ");
    scanf("%d",&n);
    float a[n];
    float b[n];
    float c[n];
    float d[n];
    float sum=0;
    float sum2;
    float sum3;
    for(int i=0;i<n;i++)
    {
        int bt;
        printf("Enter the burst time for process %d : ",i);
        scanf("%f",&a[i]);
        sum=sum+a[i];
        b[i]=sum;
        sum3=b[i]+sum3;
        d[i]=sum3;
    }
    for(int i=0;i<n;i++)
    {
        printf("Total time of %f \n",b[i]);
    }
    for(int i=0;i<n;i++)
    {
        printf("Waiting time for p%d is %f\n",i,(b[i]-a[i]));
        c[i]=b[i]-a[i];
    }
    for(int i=0;i<n;i++)
    {
        sum2=c[i]+sum2;
    }
    for(int i=0;i<n;i++)
    {
        printf("Turnaround time for p%d is : %f\n",i,d[i]);
    }
    printf("Average waiting time is : %.2f \n",sum2/n);
    printf("Average turn around time : %.2f\n",sum3/n);
}