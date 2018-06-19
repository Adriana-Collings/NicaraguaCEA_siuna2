import DT as DT
import CSection as UT

# terminal nodes
T1 = DT.TerminalNode('T1: Death after Access, Surgeon', cost=UT.T1COST, utility=UT.T1UTILITY)
T2 = DT.TerminalNode('T2: Death after Access, Surgeon, Survive, Major Complication', cost=UT.T2COST,
                     utility=UT.T2UTILITY)
T3 = DT.TerminalNode('T3: Survive after Access, Surgeon, Survive, Major Complication', cost=UT.T3COST,
                     utility=UT.T3UTILITY)
T4 = DT.TerminalNode('T4: Minor Complication after Access, Surgeon', cost=UT.T4COST, utility=UT.T4UTILITY)
T5 = DT.TerminalNode('T5: No Complication after Access, Surgeon', cost=UT.T5COST, utility=UT.T5UTILITY)
T6 = DT.TerminalNode('T6: Death after Access, Nonsuregon', cost=UT.T6COST, utility=UT.T6UTILITY)
T7 = DT.TerminalNode('T7: Death after Access, Nonsurgeon, Survive, Major Complication', cost=UT.T7COST,
                     utility=UT.T7UTILITY)
T8 = DT.TerminalNode('T8: Survive after Access, Nonsurgeon, Survive, Major Complication', cost=UT.T8COST,
                     utility=UT.T8UTILITY)
T9 = DT.TerminalNode('T9: Minor Complication after Access, Nonsurgeon, Survive', cost=UT.T9COST, utility=UT.T9UTILITY)
T10 = DT.TerminalNode('T10: No complication after Access, Nonsurgeon, Survive', cost=UT.T10COST, utility=UT.T10UTILITY)
T11 = DT.TerminalNode('T11: Death after No access', cost=UT.T11COST, utility=UT.T11UTILITY)
T12 = DT.TerminalNode('T12: Survive adter No access', cost=UT.T12COST, utility=UT.T12UTILITY)

# chance nodes
C9 = DT.ChanceNode('C9', cost=UT.C9COST, future_nodes=[T11, T12], probs=[UT.T11PROB, UT.T12PROB], utility=UT.C9UTILITY)

C8 = DT.ChanceNode('C8', cost=UT.C8COST, future_nodes=[T7, T8], probs=[UT.T7PROB, UT.T8PROB], utility=UT.C8UTILITY)

C7 = DT.ChanceNode('C7', cost=UT.C7COST, future_nodes=[C8, T7, T8, T9, T10],
                   probs=[UT.C8PROB, UT.T7PROB, UT.T8PROB, UT.T9PROB, UT.T10PROB], utility=UT.C7UTILITY)

C6 = DT.ChanceNode('C6', cost=UT.C6COST, future_nodes=[C7, C8, T6, T7, T8, T9, T10], #for some reason if you remove C8 here the whole code runs
                   probs=[UT.C7PROB, UT.C8PROB, UT.T6PROB, UT.T8PROB, UT.T9PROB, UT.T10PROB], utility=UT.C6UTILITY)

C5 = DT.ChanceNode('C5', cost=UT.C5COST, future_nodes=[T1, T2], probs=[UT.T1PROB, UT.T2PROB], utility=UT.C5UTILITY)

C4 = DT.ChanceNode('C4', cost=UT.C4COST, future_nodes=[C5, T1, T2, T3, T4], probs=[UT.C5PROB, UT.T1PROB, UT.T2PROB,
                                                                                   UT.T3PROB, UT.T4PROB],
                   utility=UT.C4UTILITY)

C3 = DT.ChanceNode('C3', cost=UT.C3COST, future_nodes=[C4, C5, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10],
                   probs=[UT.C4PROB, UT.C5PROB, UT.T1PROB, UT.T2PROB, UT.T3PROB, UT.T4PROB, UT.T5PROB, UT.T6PROB,
                          UT.T7PROB, UT.T8PROB, UT.T9PROB, UT.T10PROB], utility=UT.C3UTILITY)

C2 = DT.ChanceNode('C2', cost=UT.C2COST, future_nodes=[C3, C4, C5, C6, C7, C8, C9, T1, T2, T3, T4, T5, T6, T7, T8, T9,
                                                       T10, T11, T12],
                   probs=[UT.C3PROB, UT.C4PROB, UT.C5PROB, UT.C6PROB, UT.C7PROB, UT.C8PROB, UT.C9PROB, UT.T1PROB,
                            UT.T2PROB, UT.T3PROB, UT.T4PROB, UT.T5PROB, UT.T6PROB, UT.T7PROB, UT.T8PROB, UT.T9PROB,
                            UT.T10PROB, UT.T11PROB, UT.T12PROB], utility=UT.C2UTILITY)

C1 = DT.ChanceNode('C1', cost=UT.C1COST, future_nodes=[C2, C3, C4, C5, C6, C7, C8, C9, T1, T2, T3, T4, T5, T6, T7, T8,
                                                       T9, T10, T11, T12],
                   probs=[UT.C2PROB, UT.C3PROB, UT.C4PROB, UT.C5PROB, UT.C6PROB, UT.C7PROB, UT.C8PROB, UT.C9PROB,
                          UT.T1PROB, UT.T2PROB, UT.T3PROB, UT.T4PROB, UT.T5PROB, UT.T6PROB, UT.T7PROB, UT.T8PROB,
                          UT.T9PROB, UT.T10PROB, UT.T11PROB, UT.T12PROB], utility=UT.C1UTILITY)

# print expected cost of c1
print('C9', C9.get_expected_cost())
print('C9', C9.get_expected_utility())

print('C8', C8.get_expected_cost())
print('C8', C8.get_expected_utility())

print('C7', C7.get_expected_cost())
print('C7', C7.get_expected_utility())

print('C6', C6.get_expected_cost())
print('C6', C6.get_expected_utility())

print('C5', C5.get_expected_cost())
print('C5', C5.get_expected_utility())

print('C4', C4.get_expected_cost())
print('C4', C4.get_expected_utility())

print('C3', C3.get_expected_cost())
print('C3', C3.get_expected_utility())

print('C2', C2.get_expected_cost())
print('C2', C2.get_expected_utility())

print('C1', C1.get_expected_cost())
print('C1', C1.get_expected_utility())


