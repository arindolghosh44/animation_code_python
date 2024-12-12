#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct items{
char item[20];
float price;
int qty;

};
struct orders{
    char customer [50];
    char date[50];
    int numofitems;
struct items itm[50];
};
void generateBillHeader(char name[50],char date[30]){
    printf("\n \n");
    printf("\t SKD.Restaurent");
    printf("\n \t ------------------------------");
    printf("\n Date: %s",date);
    printf("\n Invoice to:%s",name);
    printf("\n");
    printf("---------------------------------\n");
    printf("item \t \t");
     printf("quantity \t \t");
      printf("total \t \t");
      printf("\n -----------------------------------");
      printf("\n \n");

}
void genearteBillBody(char item[67],int qty,float price)
{
printf("%s\t \t",item);
printf("%d\t\t",qty);
printf("%.2f\t\t",qty*price);
printf("\n");


}
void generateBillFooter(float total)
{
printf("\n");
float dis=0.1*total;
float nettotal=total-dis;
float cgst=0.09*nettotal,grandtotal=nettotal+2*cgst;
printf("-----------------------------------\n");
printf("Sub total\t\t\t%.2f",total);
printf("\n Discount @10%s\t\t\t%.2f","%",dis);
printf("\n \t\t\t--------------------");
printf("Net total\t\t\t%.2f",nettotal);
printf("\n Cgst @10%s\t\t\t%.2f","%",cgst);
printf("\n Sgst @10%s\t\t\t%.2f","%",cgst);
printf("\n-------------------------------------------");
printf("Grand total\t\t\t%.2f",grandtotal);
printf("\n --------------------------------------------");

}



int main()
{
    struct orders ord;
    float total;
    int o,n;
    char savebill='y';
    FILE *fp;
printf("\t =========================SKD.RESTAURENT============================");
printf("\n \n Please select your preferrred operation:\t");
printf("\n \n1.Genearte invoice:");
printf("\n 2.show all invoice:");
printf("\n 3.search  invoice:");
printf("\n 4.Exit:");
printf("\n\nYour choice:\t");
scanf("%d",&o);
fgetc(stdin);
switch(o)
{
case 1:
printf("\n Enter the  name of the customer:\t");
fgets(ord.customer,50,stdin);
ord.customer[strlen(ord.customer)-1]=0;
strcpy(ord.date,__DATE__);
printf("Enter the number of items:\t");
scanf("%d",&n);
ord.numofitems=n;
for(int i=0;i<n;i++)
{
    fgetc(stdin);
    printf("\n\n");
    printf("Please Enter the item %d",i+1);
    fgets(ord.itm[i].item,20,stdin);
    ord.itm[i].irem[strlen(ord.itm[i].item)-1]=0;
    printf("Please Enter the quentity:\t");
    scanf("%d",&ord.itm[i].qty);
    printf("Please Enter the unit price:\t");
    scanf("%f",&ord.itm[i].price);
    total+=ord.itm[i].qty*ord.itm[i].price;
}
generateBillHeader(ord.customer,ord.date);
for(int i=0;i<ord.numofitems;i++)
{
genearteBillBody(ord.itm[i].item,ord.itm[i].qty,ord.itm[i].price);


}
generateBillFooter(total);
printf("\nDo you want to save the bill:\t");
scanf("%s",&savebill);
if (savefill=='y')
{
fp=fopen("Restaurentbill.dat","a+");
fwrite(&ord,sizeof(struct orders),1,fp);
if(fwrite!=0)
printf("\n SAVED SUCCESSSFULLY");
else
printf("\n ERROR SAVING");
fclose(fp);

}
break;








}
printf("\n \n");








    return 0;


}


