# def pytest_collection_modifyitems(items):
#     """Modifies test items in place to ensure test classes run in a given order."""
#     CLASS_ORDER = [
#         "TestLogin",
#         "TestContactUs",
#         "TestLinks",
#         "TestEquityCalculator",
#         "TestValorStockLogin",
#         "TestValorStockForgot",
#         "TestAboutUs",
#         "TestLearnMore",
#         "TestAsk",
#         "TestScatteredStrategy",
#         "TestSignup",
#         "TestMyProfile",
#         "TestCalculatorLinks",
#         "TestChangePassword",
#         "TestCurrency",
#         "TestFuture",
#         "TestStrategiesLinks",
#         "TestSymmetricalStrategy",
#         "TestValorStockForumLink",
#     ]
#     class_mapping = {item: item.cls.__name__ for item in items}
#     sorted_items = items.copy()
#     # Iteratively move tests of each class to the end of the test queue
#     for class_ in CLASS_ORDER:
#         sorted_items = [it for it in sorted_items if class_mapping[it] != class_] + [
#             it for it in sorted_items if class_mapping[it] == class_
#         ]
#     items[:] = sorted_items
