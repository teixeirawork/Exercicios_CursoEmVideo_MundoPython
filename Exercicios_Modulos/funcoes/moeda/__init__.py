def aumentar(num = 0,taxa = 0):
    """_summary_

    Args:
        num (int, optional): valor do produto a ter acrescimo. Defaults to 0.
        taxa (int, optional): valor da taxa de juros a acrescentar. Defaults to 0.

    Returns:
       resultado (float): retornar o resultado do produto com juros sem formatação de moeda
    """
    
    num = float(input('Digite o valor do produto R$: '))
    taxa = float(input('Digite uma taxa de juros em %: '))
    taxa = taxa/100
    resultado = num + (num * taxa)
    
    
    return resultado


def diminuir(num = 0, taxa = 0):
    """_summary_

    Args:
        num (int, optional): valor do produto a ter desconto. Defaults to 0.
        taxa (int, optional): valor da taxa de desconto a realizar. Defaults to 0.
        
    Returns:
        resultado (float): retornar o resultado do produto com desconto sem formatação de moeda
        
    """
    num = float(input('Digite o valor do Produto R$: '))
    taxa = float(input('Digite uma taxa de juros em %: '))
    taxa = taxa/100
    resultado = num - (num * taxa)
    
    return resultado