

choise = input(
                    '''
Choose between 1 : 4
1 => Heuristic1 with Alpha & Beta,
2 => Heuristic1 without Alpha & Beta,
3 => Heuristic2 with Alpha & Beta,
4 => Heuristic2 without Alpha & Beta,
''')
    
        
if choise == '1':
    import Heuristic1_with_AB

elif choise == '2':
    import Heuristic1_without_AB

elif choise == '3':
    import Heuristic2_with_AB

elif choise == '4':
    import Heuristic2_without_AB

else:
    print("Invalid option")

