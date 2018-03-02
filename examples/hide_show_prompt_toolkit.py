# -*- coding: utf-8 -*-

"""
examples.hide_show_prompt_toolkit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage of the ``hide`` and ``show`` methods with prompt_toolkit's printing.

Requires python-prompt-tooklit (2.0):
https://github.com/jonathanslenders/python-prompt-toolkit/

.. code:: bash
    pip install -e git+https://github.com/jonathanslenders/python-prompt-toolkit@2.0#egg=python-prompt-toolkit
"""

import time

from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style
from yaspin import yaspin

# override print with feature-rich ``print_formatted_text`` from prompt_toolkit
print = print_formatted_text

# build a basic prompt_toolkit style for styling the HTML wrapped text
style = Style.from_dict({
    'msg': '#4caf50 bold',
    'sub-msg': '#616161 italic'
})


with yaspin(text='Downloading images') as spinner:

    # task 1
    time.sleep(1)
    spinner.hide()
    print(HTML(
        '<b>></b> <msg>image 1</msg> <sub-msg>download complete</sub-msg>'
    ), style=style)
    spinner.show()

    # task 2
    time.sleep(2)
    spinner.hide()
    print(HTML(
        '<b>></b> <msg>image 2</msg> <sub-msg>download complete</sub-msg>'
    ), style=style)
    spinner.show()

    # finalize
    spinner.ok()
