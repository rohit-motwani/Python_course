#include <stdio.h>
#include <stdlib.h>

void merge_sort(int low,int high)
{
    int mid;
    if(low<high)
    {
        mid=(low+high)/2;
        merge_sort(low,mid);
        merge_sort(mid+1,high);
        merge(low,mid,high);
    }
}

merge(low,mid,high)
{
    int h=low
    int i=low
    int j=mid+1
    while((h<=mid)&&(j<=high))
    {
        if(a[h]<=a[j])
        {
            b[i++]=a[h++]
        }
        else{
            b[i++]=a[j++]
        }
    }

}