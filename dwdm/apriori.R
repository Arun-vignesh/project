data("Groceries")
Groceries
summary(Groceries)
class(Groceries)
nrow(Groceries)
Groceries@itemInfo[1:20,]
apply(Groceries@data[,10:20], 2,function(r)paste(Groceries@itemInfo[r,"labels"],collapse=","))
# Frequent itemset generation for only one item
itemsets<-apriori(Groceries,parameter = list(minlen=1,maxlen=1,support=0.02,target="Frequent itemsets"))
summary(itemsets)
inspect(head(sort(itemsets,by="support"),10))

# Frequent itemset generation for two itemsets
itemsets<-apriori(Groceries,parameter = list(minlen=2,maxlen=2,support=0.02,target="Frequent itemsets"))
summary(itemsets)
inspect(head(sort(itemsets,by="support"),10))

# Frequent itemset generation for three itemsets
itemsets<-apriori(Groceries,parameter = list(minlen=3,maxlen=3,support=0.02,target="Frequent itemsets"))
summary(itemsets)
inspect(head(sort(itemsets,by="support"),10))

