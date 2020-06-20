print("hello")
v = 2L
v
class(v)
apple = c("red", "green", "yellow")
apple
list = list(1,2,3,4)
list
# Metrics
M = matrix(c("a", "b", "c","d"))
M
# Array
a = array(c("green","yellow"), dim=(3,3,2))
a
# Create a vector
apple_color = c("green", "green", "red","red")
factor_apple = factor(apple)
factor_apple


bmi = data.frame(
  gender = c("Male", "Male","Female"),
  height = c(152,171, 165),
  weight = c(81,93,78),
  Age = c(42,38,26)
)

bmi
bmi$gender
unique(bmi$gender)

cat(bmi$gender)
ls()
getcwd()

print?
?print()  


v = c(2,5.5,6)
t = c(8,3,4)
v+t
2+v

v*t

m = matrix(c(2,6,5,1,10,4), nrow = 2, ncol = 3, byrow = T)
t(m)

m = 20
if (m==20){
  print("matche")
}

fi (is.integer(m)){
  print("integer")
}

is.function(m)

# if else Function
  
c = c("what","is","truth")

if ("Truth" %in% c){
  print("Truth is Found in ")
} else {print("Truth not Found")}


x = c("What", "is","truth")
if ("truth" %in% x){
  print("Truth is found")
}


## R Switch Statement


## loop
v = c("Hello", "loop")
cnt = 2
repeat{
  print(v)
  cnt = cnt + 1
  if (cnt > 5){
    break
  }
}

## R-while loop
v = c("hello", "While loop")
cnt = 2
while (cnt <7){
  print(v)
  cnt = cnt + 1
}


v = LETTERS[1:4]


for (i in v){
  print(i)
}

# break statement
seq(1:100)

sum(1:100)
mean(1,2,3,4)



## User defined Function
new.function = function(a){
  for (i in 1:a){
    b = i^2
    print(b)
  }
}

new.function(10)


ls()
paste(v)
print(v)


a = "hello"
nchar(a)


substring(a, 2,5)

t = c("SUnday", "Monday", "Tuesday", "Thisday", "Friday")
t[c(1,2)]

v1 = c(1,4,2,5,7,10)
sort(v1)
sort(v1, decreasing = T)



lsit_data = list("krish", c(1,2,3),TRUE , FALSE)
lsit_data[c(1,2)]
c(1,2,3,5)

new_list = c(lsit_data,lsit_data)
new_list

unlist(new_list)
new_list


## Matrix
M.M = matrix(c(1:10))

M


vector = c(5,9,3)
vector2 = c(10,11,12,13,14,15)

vector+vector2


result = array(c(vector,vector2), dim = c(3,3))

result
dim(result)
max(result)

vector = c(5,9,3)
vector2 = c(10, 11,12, 13,14,15)

new_array = array(c(vector, vector2), dim = c(3,3,2))


##R-packages
.libPaths()
library()
