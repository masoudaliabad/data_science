{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7f650390",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "79b1797e",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('co22.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "00226578",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0      196\n",
       "1      221\n",
       "2      136\n",
       "3      255\n",
       "4      244\n",
       "      ... \n",
       "495    159\n",
       "496    172\n",
       "497    177\n",
       "498    244\n",
       "499    246\n",
       "Name: out1, Length: 500, dtype: int64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['out1']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "df33c962",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "134013\n",
      "268.026\n"
     ]
    }
   ],
   "source": [
    "miyangin=0\n",
    "for i in range(0,500):\n",
    "  miyangin = miyangin + df['out1'][i]\n",
    "\n",
    "print(miyangin)\n",
    "miyangin=miyangin/500\n",
    "\n",
    "print(miyangin)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
