{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "450fc335",
   "metadata": {},
   "outputs": [],
   "source": [
    "Tupla=(\"Seth\",\"Cleto\",(1,2,3,4),3.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a3a15e93",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('Seth', 'Cleto', (1, 2, 3, 4), 3.5)"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Tupla"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0f803596",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'tupla' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-3-ec45c0ae0808>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mLista\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mlist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mtupla\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'tupla' is not defined"
     ]
    }
   ],
   "source": [
    "Lista=list(tupla)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9f31bcc9",
   "metadata": {},
   "outputs": [],
   "source": [
    "Lista=list(Tupla)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "697a3aa2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Seth', 'Cleto', (1, 2, 3, 4), 3.5]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Lista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3c73c40c",
   "metadata": {},
   "outputs": [],
   "source": [
    "llaves=(1,2,3,4,5)\n",
    "Tupla=(\"Seth\",\"Cleto\",(1,2,3,4),3.5)\n",
    "Lista=list(Tupla)\n",
    "Dic=dict(zip((llaves),Lista))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fe115e42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1: 'Seth', 2: 'Cleto', 3: (1, 2, 3, 4), 4: 3.5}"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Dic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3edcdc01",
   "metadata": {},
   "outputs": [],
   "source": []
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
