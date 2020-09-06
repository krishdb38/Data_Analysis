library(datasets)
?lynx
head(lynx)
hist(lynx)
hist(lynx, breaks = 14, 
     freq = FALSE, 
     col = "thistle1",
     main = paste("Histogram of Annual Canadian Lynx","Trappings "),
     xlab = "Number of Lynx Trapped")

### Add a normal Disttion
curve(dnorm(x, mean = mean(lynx), sd = sd(lynx)),
      col="thistle4", # Color of Curve
      lwd =2, # Line width of 2 Pixel
      add = T) #Superimpose on previous graph
# Add two kernel density estimators
lines(density(lynx),col = "blue", lwd =2)
lines(density(lynx, adjust = 3), col = "purple", lwd =2)
lines(density(lynx, adjust = 3),col = "red", lwd = 2)

# Add a rug plot
rug(lynx, lwd=2, col = "gray")
head(iris)

summary(iris)

## R01_4_describe
pacman::p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis,
               httr, lubridate, plotly, rio, rmarkdown, shiny,
               stringr, tidyr)

head(iris)

p_load(psych)
p_help(psych)

describe(iris$Sepal.Length)
describe(iris)


##### Selecting Cases
#R01_4_3_SelectingCases.R
hist(iris$Petal.Length)

#Histogram virginica
hist(iris$Petal.Length[iris$Species == "virginica"],
     main ="Petal length: Virginica")


# Setosa
hist(iris$Petal.Length[iris$Species == "setosa"],
     main = "Petal Length: Setosa")

hist(iris$Petal.Length[iris$Species == "virginica" & iris$Petal.Length < 5.5],
     main = "Petal Length : Short Virginica")

# Create a Sub Symple
i.setosa = iris[iris$Species == "setosa",]
head(i.setosa)
summary(i.setosa$Petal.Length)
hist(i.setosa$Petal.Length)

###############
# Data Frame
n1 = 15
n1
l1 = T
typeof(l1)

v1 = c("a","b","c")
is.vector(v1)
v1

m1 = matrix(c(T,T,F,F,T,F),nrow = 2)
m1

########### Creating a Data Frame
vNUmeric = c(1,2,3)
vCharacter = c("a","b","c")
vLogical = c(T,F,T)
dfa = cbind(vNUmeric, vCharacter, vLogical)
dfa # All String Format
is.data.frame(dfa)
is.matrix(dfa)
df = as.data.frame(cbind(vNUmeric,vCharacter, vLogical))
df # all in its Specified Format

######## With List
o1 = c(1,2,3)
o2 = c("a","b","c")
o3 = c(T,F,T,T,F)
list1 = list(o1,o2,o3)

list2 = list(o1,o2,o3,list1) # List with in list
list1
list2

(vNUmeric)

######################
# R01_5_4 ImportingData.R
# Install and Load Packages

pacman::p_load(pacman, dplyr, GGally, ggplot2,
               ggthemes, ggvis, httr, lubridate, plotly,
               rio, rmarkdown, shiny, stringr, tidyr)

############# About File
# csv
rio_csv = import("../youtube_2/Importing_data_sets/mbb.csv")
head(rio_csv)

#### TXT
rio_txt = import("../youtube_2/Importing_data_sets/mbb.txt")
head(rio_txt)

## Excel
rio_xlsx = import("../youtube_2/Importing_data_sets/mbb.xlsx")
head(rio_xlsx)


### View 
View(rio_csv) # Only to display

#### Using to read.table Function
trends.csv = read.csv("../youtube_2/Importing_data_sets/mbb.csv",
                      header = T)
 
##### r01_6_1 Hierarchical Clustering.R

pacman:: p_load(pacman, dplyr, GGally, ggplot2, ggthemes, ggvis,
                httr, lubridate, plotly, rio, rmarkdown, shiny,
                stringr,tidyr)

library(datasets)

### Load the Data Set
head(mtcars)
# ?mtcars
hc = cars %>% # Get Cars data
     dist %>%
     hclust

## Add Boxes to Plot
rect.hclust(hc, k=2, border = "red")
rect.hclust(hc,k=3, border = "blue")
rect.hclust(hc, k = 4, border = "green")
rect.hclust(hc,k=5, border = "darkred")

##### Principle Component Analysis
# Loading the packages using pacman
pacman::p_load(pacman, dplyr,GGally, ggplot2,ggthemes,ggvis, httr, lubridate,
               plotly,rio, rmarkdown, shiny, stringr, tidyr)

library(datasets)

head(mtcars)
## Creating subsets
cars = mtcars[,c(1:4,6:7,9:11)] # selecting variables
head(cars)
colnames(mtcars)

### COMPUTE PCA 
# For Entire data Frame 
pc = prcomp(cars, center  = T, #Centre means to 0 ,
            scale = T) # Sets unit variance (helpful)
pc

## Applying selected Variable
pc = prcomp(~ mpg+cyl+disp+ hp + wt + qsec + am + gear + carb,
            data = mtcars,
            center = T,
            scale = T)
pc
head(pc)

summary(pc)

plot(pc)

# See how cases load on PCS
predict(pc) %>% round(2)

# Biplot of first two components
biplot(pc)



################## Regression

# Loading the packages using pacman
pacman::p_load(pacman, dplyr,GGally, ggplot2,ggthemes,ggvis, httr, lubridate,
               plotly,rio, rmarkdown, shiny, stringr, tidyr)
library(datasets)

##########
# Load data sets
?USJudgeRatings
head(USJudgeRatings)

data = USJudgeRatings
# Define variable groups
x = as.matrix(data[-12]) # All Except 12
y = data[,12]  # Only 12

## Using variable groups
reg1 = lm(y~x)

## Or specify variables individually
colnames(USJudgeRatings)
reg1 = lm(RTEN~CONT+INTG+ DMNR + DILG + CFMG + DECI 
          + PREP + FAMI + ORAL + WRIT + PHYS,data = USJudgeRatings)
summary(reg1)


#################### Use two Conditional libraries
p_load(lars, caret)


## Conditional Step wise regression
stepwise = lars(x,y,type = "stepwise")

# Stagewise : Like stepwise but with better generalizability
forward = lars(x,y,type = "forward.stagewise")

# LAR: Least Angle Regression
lar = lars(x,y,type = "lar")

## LASSO: Least Absolute Shrinkage and Selection Operator
lasso = lars(x,y, type = "lasso")

# Comparison of R^2 for new models
r2comp = c(stepwise$R2[6],forward$R2[6],lar$R2[6], lasso$R2[6]) %>%round(2)
r2comp




