#We are working at AwesomeBank3000, where the manager has an idea for fraud detection. 
#He thinks everyone with a salary over 555000 who pays less than 30% tax-rate, is worth investigating 
#(tax-rate= taxes/salary). The customers database is huge, so you only take a small sample of the data into 
#python and try to see if you can make the logic for a program that prints the name of those who fit this category. 



#the first customer (‘James’) has the first salary (155000) with the first taxes (55800), the second person (‘John’)
# has the second salary and taxes values etc…
#add the following logic to the file such that it prints the name of anyone in the fraud category 
#defined by you manager.


customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salary = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]



def low_taxes(customers, salary, taxes):
    low_taxes = []
    for i in range(0, len(customers)):
        if taxes[i] / salary[i] < 0.3:
            low_taxes.append(customers[i])
        else: 
            pass
        
    print(low_taxes)
    
    
    