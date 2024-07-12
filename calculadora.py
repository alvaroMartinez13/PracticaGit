from main import *

def suma():
    num1 = int(input("ingrese numero 1: "))
    num2 = int(input("ingrese numero 1: "))
    num3 = num1 + num2
    return num3

def multipliccion():
    num1 = int(input("ingrese numero 1: "))
    num2 = int(input("ingrese numero 1: "))
    num3 = num1 * num2
    return num3def resta(num1, num2):
    return num1-num2

def division(num1, num2):
    if num2 == 0:
        return "Error"
    return num1/num2