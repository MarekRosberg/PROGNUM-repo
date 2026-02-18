{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3054600b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The 100th Fibonacci term is: 354224848179261915075\n"
     ]
    }
   ],
   "source": [
    "a = 0\n",
    "b = 1\n",
    "\n",
    "for i in range(99):\n",
    "    c = a + b\n",
    "    a = b\n",
    "    b = c\n",
    "\n",
    "print(\"The 100th Fibonacci term is:\", c)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "649f48a8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
