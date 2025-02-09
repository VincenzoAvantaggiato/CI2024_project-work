# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np


def f0(x: np.ndarray) -> np.ndarray:
    return np.add(x[0], np.multiply(-0.140281, np.multiply(np.subtract(-0.400897, np.cos(np.multiply(np.sin(np.cos(x[1])), np.subtract(np.multiply(x[1], x[1]), np.multiply(np.multiply(np.sin(x[1]), 0.426575), np.multiply(np.subtract(-0.140281, np.cos(np.multiply(np.sin(x[1]), np.subtract(1.25265, np.multiply(np.multiply(np.sin(x[1]), 0.426575), np.multiply(np.subtract(-0.140281, np.multiply(np.multiply(np.sin(x[1]), 0.426575), np.multiply(np.subtract(-0.140281, np.sin(np.subtract(np.subtract(0.916315, np.sin(np.sin(np.multiply(1.28782, x[1])))), np.multiply(-0.140281, x[1])))), np.multiply(1.28782, x[1])))), np.multiply(1.28782, x[1]))))))), x[1])))))), x[1])))
    return x[0] + np.sin(x[1]) / 5

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    return np.add(np.multiply(np.add(np.multiply(np.multiply(x[0], np.sin(-0.898513)), 0.0545983), np.add(x[0], np.add(1.28009, np.sinh(np.multiply(np.exp(1.68327), np.add(0.987022, np.multiply(-1.69614, np.tanh(-1.56689)))))))), x[2]), np.multiply(np.add(x[1], np.add(np.add(0.987022, np.multiply(-1.69614, np.tanh(x[0]))), np.subtract(np.sinh(np.multiply(np.exp(1.68327), 1.7515)), np.add(np.multiply(1.70039, np.add(0.36735, np.cosh(np.add(x[2], x[0])))), np.cosh(np.add(np.multiply(0.328658, x[0]), np.add(x[2], x[1]))))))), np.add(np.multiply(np.exp(x[1]), 1.7515), np.add(x[0], np.add(np.exp(x[1]), np.multiply(x[0], np.exp(np.exp(1.68327))))))))

def f3(x: np.ndarray) -> np.ndarray:
    return np.add(np.subtract(np.multiply(np.sin(0.516614), np.subtract(np.subtract(x[1], x[1]), x[2])), x[2]), np.add(np.subtract(np.sin(np.multiply(1.0099, 0.799579)), x[2]), np.add(np.subtract(np.sin(0.729197), x[2]), np.add(1.38768, np.add(np.multiply(x[0], x[0]), np.add(np.multiply(x[0], x[0]), np.add(np.multiply(np.multiply(np.multiply(x[1], np.cos(-1.23315)), np.sin(np.multiply(1.11106, np.multiply(1.0099, 0.729197)))), 0.799579), np.add(np.subtract(1.19791, x[1]), np.multiply(np.subtract(0.799579, np.multiply(x[1], x[1])), x[1])))))))))

def f4(x: np.ndarray) -> np.ndarray:
    return np.add(np.cos(np.multiply(1.37954, -0.295438)), np.add(-1.44507, np.add(np.add(np.cos(x[1]), np.add(1.37954, np.add(np.add(np.cos(np.cos(np.subtract(np.add(np.multiply(0.0632359, np.multiply(-0.891081, np.multiply(-1.4886, np.multiply(-0.946446, np.multiply(-1.4886, np.cos(np.multiply(np.subtract(0.859964, x[0]), np.cos(np.subtract(-0.946446, np.cos(np.subtract(0.591412, np.cos(np.add(np.multiply(0.0632359, np.multiply(0.0569691, np.multiply(-1.4886, np.cos(np.multiply(x[1], np.cos(np.cos(np.subtract(np.multiply(0.0569691, np.multiply(np.subtract(-0.946446, np.cos(np.subtract(0.591412, np.cos(np.cos(np.subtract(0.591412, np.cos(np.multiply(1.42285, np.add(np.multiply(np.cos(np.subtract(-0.946446, np.cos(-0.295438))), np.subtract(np.cos(x[1]), x[1])), np.add(np.add(np.cos(x[1]), np.add(1.37954, np.add(np.add(np.cos(np.cos(np.subtract(-0.946446, np.cos(np.add(np.multiply(0.0632359, np.multiply(-0.891081, np.multiply(-1.4886, np.cos(np.cos(np.subtract(np.cos(np.multiply(np.subtract(0.859964, x[0]), np.cos(x[1]))), np.cos(-0.295438))))))), -0.891081))))), np.add(np.cos(x[1]), np.cos(x[1]))), np.add(np.cos(0.591412), np.add(0.859964, np.add(-0.00216417, np.cos(x[1]))))))), np.add(np.cos(x[1]), np.add(np.cos(np.subtract(np.multiply(0.0569691, np.multiply(np.subtract(-0.946446, np.cos(np.subtract(np.cos(np.cos(np.subtract(np.multiply(0.0569691, np.multiply(np.subtract(-0.946446, np.cos(np.subtract(0.591412, np.cos(np.cos(np.subtract(0.591412, np.multiply(np.subtract(0.859964, x[0]), np.cos(x[1])))))))), x[0])), np.cos(np.subtract(np.subtract(x[0], x[0]), -0.295438))))), np.cos(np.cos(np.subtract(0.591412, np.cos(np.multiply(np.cos(np.subtract(-0.946446, np.cos(np.add(np.multiply(0.0632359, np.multiply(-0.891081, np.multiply(np.cos(np.multiply(x[1], np.cos(x[1]))), np.cos(np.add(-1.25967, np.subtract(x[0], 1.60493)))))), -0.891081)))), np.add(np.multiply(np.cos(np.subtract(-0.946446, np.cos(-0.295438))), np.subtract(-0.386744, x[1])), 0.0569691))))))))), x[0])), np.multiply(-1.50655, np.cos(np.subtract(np.subtract(np.sin(x[1]), np.add(0.678777, x[0])), -0.295438))))), np.cos(x[1]))))))))))))), x[0])), np.cos(np.subtract(np.subtract(x[0], x[0]), -0.295438)))))))))), -0.891081))))))))))))), -0.891081), np.cos(np.add(np.multiply(0.0632359, np.multiply(0.0569691, np.multiply(-1.4886, np.cos(np.subtract(np.multiply(0.0569691, np.multiply(np.multiply(0.545816, np.subtract(-0.946446, np.cos(np.subtract(0.591412, np.cos(np.cos(np.subtract(0.591412, np.cos(np.multiply(1.42285, np.add(np.multiply(x[0], np.subtract(np.cos(x[1]), x[1])), np.add(np.add(np.cos(x[1]), np.add(1.37954, np.add(np.add(np.cos(np.cos(np.subtract(-0.946446, 0.859964))), np.add(np.cos(x[1]), np.cos(x[1]))), np.add(np.cos(x[1]), np.add(0.859964, np.add(-0.00216417, np.cos(x[1]))))))), np.add(np.cos(x[1]), np.add(np.cos(np.subtract(np.multiply(0.0569691, np.multiply(np.subtract(-0.946446, np.cos(np.subtract(0.591412, np.cos(np.cos(np.subtract(0.591412, np.cos(np.multiply(np.cos(np.subtract(-0.946446, np.cos(np.add(np.multiply(0.0632359, np.multiply(-0.891081, np.subtract(x[1], np.multiply(np.cos(np.multiply(x[1], np.cos(x[1]))), np.cos(np.add(-1.25967, np.subtract(np.cos(x[1]), 1.60493))))))), -0.891081)))), np.add(np.multiply(np.cos(np.subtract(np.cos(np.multiply(np.subtract(0.859964, x[0]), np.cos(x[1]))), np.cos(-0.295438))), np.subtract(-0.386744, x[1])), 0.0569691))))))))), x[0])), np.cos(np.subtract(np.subtract(np.sin(x[1]), np.add(0.678777, x[0])), -0.295438)))), np.cos(x[1])))))))))))))), x[0])), np.multiply(x[0], np.cos(np.subtract(np.subtract(-0.386744, x[0]), -0.295438)))))))), -0.891081))))), np.add(np.cos(x[1]), np.cos(x[1]))), np.add(np.cos(x[1]), np.add(0.859964, np.add(-0.00216417, np.cos(x[1]))))))), np.add(np.cos(x[1]), np.add(np.cos(np.subtract(np.multiply(0.0569691, np.multiply(np.subtract(-0.946446, np.cos(np.subtract(0.591412, np.cos(np.add(np.multiply(0.0632359, np.multiply(0.0569691, np.multiply(-1.4886, np.cos(np.cos(x[1]))))), -0.891081))))), x[0])), np.cos(np.subtract(np.subtract(x[0], np.add(0.678777, x[0])), -0.295438)))), np.cos(x[1]))))))

def f5(x: np.ndarray) -> np.ndarray:
    return np.multiply(x[0], np.multiply(0.363602, np.multiply(np.add(np.subtract(x[0], 0.363602), np.cos(x[0])), np.multiply(np.cos(-1.50301), np.multiply(0.363602, np.multiply(np.multiply(np.multiply(np.multiply(np.subtract(x[1], 0.698396), np.multiply(np.cos(-1.50301), np.exp(-1.50301))), np.multiply(0.363602, np.multiply(np.add(x[0], np.subtract(x[1], 0.698396)), np.multiply(np.multiply(np.cos(-1.50301), np.multiply(np.subtract(x[1], np.subtract(np.cos(np.exp(np.subtract(-1.52497, x[1]))), -0.256538)), np.multiply(np.cos(-1.50301), np.exp(-1.50301)))), np.multiply(np.multiply(np.subtract(x[1], np.cos(np.add(x[0], x[1]))), np.multiply(np.cos(-1.50301), np.exp(-1.80762))), np.exp(-1.77607)))))), np.cos(-1.77607)), np.multiply(np.multiply(np.subtract(np.cos(np.cos(np.subtract(x[1], 0.698396))), np.cos(-1.77607)), np.exp(-1.50301)), np.exp(-1.50301))))))))

def f6(x: np.ndarray) -> np.ndarray:
    return np.add(np.multiply(np.sin(0.784181), x[1]), np.subtract(np.add(np.multiply(1.34051, np.multiply(x[1], np.multiply(np.cos(x[1]), np.multiply(x[0], np.subtract(x[0], x[0]))))), x[1]), np.add(np.multiply(np.subtract(np.add(0.784181, -0.0506562), 0.784181), np.subtract(0.560634, np.multiply(0.0874461, np.subtract(np.add(1.94535, np.add(x[1], np.cos(np.add(np.multiply(np.subtract(np.add(np.add(x[1], np.add(np.subtract(x[1], np.multiply(x[1], np.add(x[1], np.multiply(np.subtract(np.cos(x[1]), np.multiply(np.subtract(0.560634, np.multiply(0.0874461, np.add(x[1], np.subtract(np.add(1.94535, np.add(x[1], np.cos(np.add(np.multiply(0.784181, -0.0506562), np.multiply(x[0], np.subtract(0.587439, x[0])))))), np.add(np.subtract(-1.86602, x[0]), np.subtract(np.multiply(x[0], 1.79658), x[1])))))), np.sin(0.784181))), np.add(np.multiply(np.subtract(np.add(0.784181, -0.0506562), 0.784181), np.subtract(np.add(np.multiply(1.34051, np.multiply(x[1], np.multiply(np.cos(x[1]), np.subtract(0.560634, np.multiply(0.0874461, np.subtract(np.add(1.94535, np.add(x[1], np.cos(np.add(np.multiply(np.subtract(np.add(np.add(np.subtract(x[1], np.multiply(x[1], np.add(x[1], np.multiply(np.subtract(np.cos(np.multiply(0.109979, -1.22475)), np.multiply(np.subtract(x[1], np.multiply(0.0874461, np.add(x[1], np.subtract(np.add(1.94535, np.add(np.multiply(np.subtract(x[1], np.cos(np.subtract(0.587439, x[0]))), np.multiply(x[0], np.subtract(np.add(np.multiply(np.subtract(np.add(0.784181, -0.0506562), -0.0506562), x[1]), np.multiply(x[0], np.sin(0.784181))), x[0]))), np.subtract(0.539703, np.cos(np.add(np.multiply(0.784181, -0.0506562), np.add(np.multiply(np.subtract(0.438263, x[0]), np.multiply(np.multiply(x[0], -1.135), np.multiply(np.cos(x[1]), np.multiply(np.multiply(x[0], np.subtract(x[0], x[0])), np.subtract(x[0], x[0]))))), np.cos(np.multiply(x[1], np.multiply(np.cos(x[1]), np.multiply(x[0], np.subtract(x[0], x[0]))))))))))), np.add(np.subtract(-1.86602, -0.593448), np.subtract(np.multiply(x[0], np.add(1.45885, np.multiply(x[1], np.multiply(np.cos(x[1]), np.multiply(np.sin(-1.07768), np.subtract(x[0], x[0])))))), np.cos(x[0]))))))), np.sin(0.784181))), np.add(x[1], np.subtract(x[0], 0.784181)))))), x[1]), np.subtract(np.add(x[1], x[0]), -0.696719)), 0.784181), -0.0506562), np.multiply(np.multiply(0.0874461, np.add(0.471485, x[0])), -0.0506562))))), np.add(-0.83792, np.add(-1.02933, np.subtract(np.multiply(x[0], np.add(1.45885, np.cos(np.multiply(x[1], np.multiply(np.multiply(1.79658, np.subtract(-0.811335, np.cos(x[1]))), np.multiply(x[0], np.subtract(x[0], x[0]))))))), x[1]))))))))), x[1]), np.multiply(0.0874461, np.subtract(np.multiply(x[1], np.add(1.94535, np.add(1.4523, np.add(x[1], np.cos(np.add(np.multiply(np.subtract(np.add(np.add(np.subtract(x[1], np.multiply(x[1], np.add(x[1], np.multiply(np.subtract(np.cos(x[1]), np.multiply(np.add(np.multiply(np.subtract(np.add(-1.71706, np.add(0.784181, -0.0506562)), -0.0506562), x[1]), np.multiply(x[0], np.sin(0.784181))), np.sin(np.multiply(1.79522, 0.134326)))), np.add(np.sin(x[1]), np.subtract(x[0], 0.784181)))))), x[1]), np.subtract(np.add(x[1], x[0]), -0.696719)), 0.784181), -0.0506562), np.multiply(np.multiply(-1.37784, np.add(x[1], np.multiply(np.subtract(np.cos(x[1]), np.multiply(np.add(np.multiply(np.subtract(np.add(0.784181, -0.0506562), 0.784181), np.subtract(0.560634, np.multiply(0.0874461, np.subtract(np.add(1.94535, np.add(x[1], np.cos(np.add(np.multiply(np.subtract(np.add(np.add(np.subtract(x[1], np.multiply(x[1], np.add(np.sin(-0.609639), np.multiply(np.subtract(np.cos(x[1]), x[0]), np.add(x[1], np.subtract(x[0], 0.784181)))))), x[1]), np.subtract(np.add(x[1], x[0]), -0.696719)), 0.784181), -0.0506562), np.multiply(np.multiply(0.0874461, np.add(0.471485, x[0])), -0.0506562))))), np.add(-0.83792, np.add(-1.02933, np.subtract(np.multiply(x[0], np.add(1.45885, np.cos(np.multiply(x[1], np.multiply(np.multiply(1.79658, np.subtract(-0.811335, np.cos(x[1]))), np.multiply(x[0], np.subtract(x[0], x[0]))))))), x[1]))))))), np.multiply(x[0], np.sin(0.784181))), np.sin(0.784181))), np.add(0.341927, np.subtract(x[0], 0.784181))))), -0.0506562))))))), np.add(-0.83792, np.add(-1.02933, np.multiply(np.add(-0.630949, -0.311697), np.subtract(np.multiply(x[0], np.add(1.45885, np.cos(np.multiply(x[1], np.multiply(np.add(np.subtract(-1.86602, -0.593448), np.subtract(np.multiply(x[0], np.add(1.45885, np.multiply(x[1], np.add(1.83933, np.multiply(np.cos(x[1]), np.multiply(x[0], np.subtract(x[0], x[0]))))))), np.cos(x[0]))), np.multiply(x[0], np.subtract(x[0], x[0]))))))), np.sin(1.06108))))))))), np.multiply(x[0], np.sin(0.784181))))))), x[1])), np.subtract(x[0], -0.696719)), np.subtract(x[1], x[1])), -0.0506562), np.multiply(np.multiply(-1.37784, np.add(np.multiply(1.94535, np.sin(x[1])), x[0])), -0.0506562))))), np.add(-0.83792, np.add(-1.02933, np.subtract(np.multiply(x[0], np.add(1.45885, np.cos(np.multiply(x[1], np.multiply(np.cos(x[1]), np.multiply(x[0], np.subtract(x[0], x[0]))))))), x[1]))))))), np.multiply(x[0], np.sin(0.784181)))))

def f7(x: np.ndarray) -> np.ndarray:
    return np.cosh(np.subtract(-0.169562, np.subtract(-0.381632, np.add(np.multiply(x[0], x[1]), np.exp(np.cos(np.multiply(np.add(np.multiply(x[0], x[1]), np.exp(np.cos(np.cosh(0.00138594)))), np.subtract(x[0], x[1]))))))))

def f8(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.add(-1.73296, np.add(-0.991745, np.sinh(x[5]))), np.add(np.cosh(np.exp(1.68681)), np.exp(np.exp(1.48789))))
    

