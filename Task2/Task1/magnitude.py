{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2b146160",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "unsupported operand type(s) for -: 'str' and 'str'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[14], line 11\u001b[0m\n\u001b[1;32m      3\u001b[0m absoluteMagnitude \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m1.45\u001b[39m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;66;03m# The distance is related to the magnitudes as m-M=5.Log(d/10)\u001b[39;00m\n\u001b[1;32m      6\u001b[0m \u001b[38;5;66;03m# 1 Parsec = 3.26164 ly\u001b[39;00m\n\u001b[1;32m      7\u001b[0m \n\u001b[1;32m      8\u001b[0m \u001b[38;5;66;03m#m = apparentMagnitude\u001b[39;00m\n\u001b[1;32m      9\u001b[0m \u001b[38;5;66;03m#M = absoluteMagnitude\u001b[39;00m\n\u001b[0;32m---> 11\u001b[0m d1 \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m10.0\u001b[39m \u001b[38;5;241m*\u001b[39m \u001b[38;5;28mpow\u001b[39m( \u001b[38;5;241m10.0\u001b[39m, (\u001b[43mm\u001b[49m\u001b[38;5;241;43m-\u001b[39;49m\u001b[43mM\u001b[49m)\u001b[38;5;241m/\u001b[39m\u001b[38;5;241m5.0\u001b[39m ) \u001b[38;5;241m*\u001b[39m \u001b[38;5;241m3.26164\u001b[39m\n\u001b[1;32m     12\u001b[0m a \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapparent magnitude: \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m     13\u001b[0m b \u001b[38;5;241m=\u001b[39m \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mabsolute magnitude: \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[0;31mTypeError\u001b[0m: unsupported operand type(s) for -: 'str' and 'str'"
     ]
    }
   ],
   "source": [
    "# Sirius data\n",
    "apparentMagnitude = -1.46\n",
    "absoluteMagnitude = 1.45\n",
    "\n",
    "# The distance is related to the magnitudes as m-M=5.Log(d/10)\n",
    "# 1 Parsec = 3.26164 ly\n",
    "\n",
    "#m = apparentMagnitude\n",
    "#M = absoluteMagnitude\n",
    "\n",
    "d1 = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164\n",
    "a = input(\"apparent magnitude: \")\n",
    "b = input(\"absolute magnitude: \")\n",
    "x1 = float(a)\n",
    "x2 = float(b)\n",
    "print(\"The distance to the star with the apparent magnitude\",x1, \"and absolute magnitude\",x2, \"is\", d1)\n",
    "print(\"The distance of Sirius is 8.61\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f07e33a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47952592",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9879029",
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
