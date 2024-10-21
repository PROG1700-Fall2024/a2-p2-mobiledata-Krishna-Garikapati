#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: Krishna Priyanka Garikapati    
#Student Name:  W0502117

def main():
    #input
        DataUsage=int(input("Enter data usage (Mb): "))
    #Conditions
        if DataUsage<=200:
            TotalCharge=20
        elif 500>=DataUsage>200:
            TotalCharge=20+((DataUsage-200)*0.105)+1
        elif 1000>=DataUsage>500:
            TotalCharge=20+(300*(0.105))+((DataUsage-500)*0.105)
        elif DataUsage>1000:
            TotalCharge=118.00
    #Output
        print("Total charge is ${0:.2f}".format(TotalCharge) )
main()