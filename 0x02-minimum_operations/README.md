# Minimum Operations
## General Case
For any number ( n ):
- The prime factorization of ( n ) gives you the sequence of multiplications needed to reach ( n ).

- The sum of these factors corresponds to the total number of operations because each factor contributes to the number of times you need to multiply the current number of ‘H’ characters.

- **fewest number of operations needed  = sum(prime factorization(n))**

### BUT Why Operations = Sum of Factors 🤔❔
#### Building Up with Multiplication:
- Each prime factor represents a step where you multiply the current number of ‘H’ characters.
- For example, multiplying by 2 means you double the number of ‘H’ characters, which corresponds to one “Copy All” and one “Paste”.
- ex Prime factorization breaks down ( n ) into its prime factors. For example, ( n = 12 ) can be factorized as ( 2 \times 2 \times 3 ).
