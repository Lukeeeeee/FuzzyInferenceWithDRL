### inputVariable
#### input: obeserved value of each variable
#### output: degree of its all linguistic label

#### attribute 
1. value  [float] 
2. name string
3. linguistic_label [string]
4. mf [MembershipFunction]
5. degree [float]
6. upper_range float
7. lower_range float

#### method
1. set_value(new_value) //set the value of variable 
2. calc_degree() //calc the degree based on the value w.r.t every linguistic label


### outputVariable
#### input: the degree after reasoned by a set of rule of all its linguistic label
#### output: action value computed by defuzzifier

#### attribute
1. value  [float] 
2. name string
3. linguistic_label [string]
4. mf [MembershipFunction]
5. degree [float]
6. upper_range float
7. lower_range float
8. defuzzifier
### method
1. set_degree(new_degree) // set the degree of output val of all its linguistic label
2. calc_value() //calc the action or value based on the defuzzifizer and degree