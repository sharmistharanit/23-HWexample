{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "55299c01-d2dd-420f-ad38-bc8e7b1084ee",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
     ]
    }
   ],
   "source": [
    "def fibonacci(n):\n",
    "    \n",
    "    fib_series = [0, 1]\n",
    "\n",
    "    \n",
    "    while len(fib_series) < n:\n",
    "        next_number = fib_series[-1] + fib_series[-2]\n",
    "        fib_series.append(next_number)\n",
    "\n",
    "    return fib_series\n",
    "\n",
    "\n",
    "num_terms = 10  \n",
    "\n",
    "\n",
    "result = fibonacci(num_terms)\n",
    "print(result)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f679e200-37e6-4a8b-a036-6e11fa972452",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Traceback \u001b[1;36m(most recent call last)\u001b[0m:\n",
      "\u001b[1;36m  File \u001b[1;32m/opt/conda/lib/python3.10/site-packages/IPython/core/compilerop.py:86\u001b[1;36m in \u001b[1;35mast_parse\u001b[1;36m\n",
      "\u001b[1;33m    return compile(source, filename, symbol, self.flags | PyCF_ONLY_AST, 1)\u001b[1;36m\n",
      "\u001b[1;36m  Cell \u001b[1;32mIn[5], line 1\u001b[1;36m\u001b[0m\n",
      "\u001b[1;33m    git clone <https://github.com/sharmistharanit/23-HWexample/commit/acc9ed8c7d37e8ab03931d5160019259281d00b3>\u001b[0m\n",
      "\u001b[1;37m        ^\u001b[0m\n",
      "\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n",
      "\n",
      "Use %tb to get the full traceback.\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "\n",
       "<style>\n",
       ".button {\n",
       "  border: none;\n",
       "  color: white;\n",
       "  padding: 4px 8px;\n",
       "  text-align: center;\n",
       "  text-decoration: none;\n",
       "  display: inline-block;\n",
       "  font-size: 12px;\n",
       "  margin: 4px 2px;\n",
       "  transition-duration: 0.2s;\n",
       "  cursor: pointer;\n",
       "}\n",
       ".iqx-button {\n",
       "  background-color: #0f62fe; \n",
       "  color: white; \n",
       "}\n",
       ".iqx-button:hover {\n",
       "  background-color: #0043ce;\n",
       "  color: white;\n",
       "}\n",
       "</style>\n",
       "<a href=\"https://stackoverflow.com/search?q=SyntaxError: invalid syntax\" target='_blank'><button class='button iqx-button'>Search for solution online</button></a>\n"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c588bf89-3a6b-48bf-9bbc-bab2874f732d",
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
   "version": "3.10.8"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
