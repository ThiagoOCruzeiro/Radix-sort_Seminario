def counting_sort(arr, exp):
    n = len(arr)                          
    saida = [0] * n                       
    contagem = [0] * 10                   
    for i in range(n):                    
        digito = (arr[i] // exp) % 10     
        contagem[digito] += 1             

    for i in range(1, 10):                
        contagem[i] += contagem[i - 1]    

    for i in range(n - 1, -1, -1):        
        digito = (arr[i] // exp) % 10     
        saida[contagem[digito] - 1] = arr[i]  
        contagem[digito] -= 1             

    for i in range(n):                    
        arr[i] = saida[i]


def radix_sort_positivos(arr):
    if not arr:                           
        return
    maior = max(arr)                      
    exp = 1                               

    while maior // exp > 0:               
        counting_sort(arr, exp)           
        exp *= 10                         


def radix_sort(arr):
    negativos = [-n for n in arr if n < 0]   
    positivos = [n for n in arr if n >= 0]   

    radix_sort_positivos(negativos)          
    radix_sort_positivos(positivos)          

    negativos = [-n for n in reversed(negativos)]  

    return negativos + positivos             


numeros = [170, -45, 75, -90, 802, 24, -2, 66]  
numeros = radix_sort(numeros)                   
print(numeros)                                  