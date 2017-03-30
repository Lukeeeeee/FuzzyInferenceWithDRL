###  Pipeline for reasoning of one section
1. Assume we have a fuzzy logic rule already.
2. Get the real value of input variable.
3. inputVariable.calc_antecedent() -> mf.calc()
4. fuzzyRule.get_true_value() -> fuzzyRule.min_op()
5. defuzzifier.defuzzy()
6. fuzzyRuleSet.calc_average_output()
7. Get the final value of action