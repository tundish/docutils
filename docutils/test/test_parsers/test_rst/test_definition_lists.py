#! /usr/bin/env python

"""
:Author: David Goodger
:Contact: goodger@users.sourceforge.net
:Revision: $Revision$
:Date: $Date$
:Copyright: This module has been placed in the public domain.

Tests for states.py.
"""

from __init__ import DocutilsTestSupport

def suite():
    s = DocutilsTestSupport.ParserTestSuite()
    s.generateTests(totest)
    return s

totest = {}

totest['definition_lists'] = [
["""\
term
  definition
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term
            <definition>
                <paragraph>
                    definition
"""],
["""\
term
  definition

paragraph
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term
            <definition>
                <paragraph>
                    definition
    <paragraph>
        paragraph
"""],
["""\
term
  definition
no blank line
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term
            <definition>
                <paragraph>
                    definition
    <system_message level="2" line="3" source="test data" type="WARNING">
        <paragraph>
            Definition list ends without a blank line; unexpected unindent.
    <paragraph>
        no blank line
"""],
["""\
A paragraph::
    A literal block without a blank line first?
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                A paragraph::
            <definition>
                <system_message level="1" line="2" source="test data" type="INFO">
                    <paragraph>
                        Blank line missing before literal block? Interpreted as a definition list item.
                <paragraph>
                    A literal block without a blank line first?
"""],
["""\
this is not a term;
a term may only be one line long
  this is not a definition
""",
"""\
<document source="test data">
    <paragraph>
        this is not a term;
        a term may only be one line long
    <system_message level="3" line="3" source="test data" type="ERROR">
        <paragraph>
            Unexpected indentation.
    <block_quote>
        <paragraph>
            this is not a definition
"""],
["""\
term 1
  definition 1

term 2
  definition 2
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term 1
            <definition>
                <paragraph>
                    definition 1
        <definition_list_item>
            <term>
                term 2
            <definition>
                <paragraph>
                    definition 2
"""],
["""\
term 1
  definition 1 (no blank line below)
term 2
  definition 2
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term 1
            <definition>
                <paragraph>
                    definition 1 (no blank line below)
        <definition_list_item>
            <term>
                term 2
            <definition>
                <paragraph>
                    definition 2
"""],
["""\
term 1
  definition 1 (no blank line below)
term 2
  definition 2
No blank line after the definition list.
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term 1
            <definition>
                <paragraph>
                    definition 1 (no blank line below)
        <definition_list_item>
            <term>
                term 2
            <definition>
                <paragraph>
                    definition 2
    <system_message level="2" line="5" source="test data" type="WARNING">
        <paragraph>
            Definition list ends without a blank line; unexpected unindent.
    <paragraph>
        No blank line after the definition list.
"""],
["""\
term 1
  definition 1

  term 1a
    definition 1a

  term 1b
    definition 1b

term 2
  definition 2

paragraph
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                term 1
            <definition>
                <paragraph>
                    definition 1
                <definition_list>
                    <definition_list_item>
                        <term>
                            term 1a
                        <definition>
                            <paragraph>
                                definition 1a
                    <definition_list_item>
                        <term>
                            term 1b
                        <definition>
                            <paragraph>
                                definition 1b
        <definition_list_item>
            <term>
                term 2
            <definition>
                <paragraph>
                    definition 2
    <paragraph>
        paragraph
"""],
["""\
Term : classifier
    The ' : ' indicates a classifier in
    definition list item terms only.
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                Term
            <classifier>
                classifier
            <definition>
                <paragraph>
                    The ' : ' indicates a classifier in
                    definition list item terms only.
"""],
["""\
Term: not a classifier
    Because there's no space before the colon.
Term :not a classifier
    Because there's no space after the colon.
Term \: not a classifier
    Because the colon is escaped.
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                Term: not a classifier
            <definition>
                <paragraph>
                    Because there's no space before the colon.
        <definition_list_item>
            <term>
                Term :not a classifier
            <definition>
                <paragraph>
                    Because there's no space after the colon.
        <definition_list_item>
            <term>
                Term : not a classifier
            <definition>
                <paragraph>
                    Because the colon is escaped.
"""],
["""\
Term `with *inline ``text **errors : classifier `with *errors ``too
    Definition `with *inline ``text **markup errors.
""",
"""\
<document source="test data">
    <definition_list>
        <definition_list_item>
            <term>
                Term \n\
                <problematic id="id2" refid="id1">
                    `
                with \n\
                <problematic id="id4" refid="id3">
                    *
                inline \n\
                <problematic id="id6" refid="id5">
                    ``
                text \n\
                <problematic id="id8" refid="id7">
                    **
                errors
            <classifier>
                classifier \n\
                <problematic id="id10" refid="id9">
                    `
                with \n\
                <problematic id="id12" refid="id11">
                    *
                errors \n\
                <problematic id="id14" refid="id13">
                    ``
                too
            <definition>
                <system_message backrefs="id2" id="id1" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline interpreted text or phrase reference start-string without end-string.
                <system_message backrefs="id4" id="id3" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline emphasis start-string without end-string.
                <system_message backrefs="id6" id="id5" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline literal start-string without end-string.
                <system_message backrefs="id8" id="id7" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline strong start-string without end-string.
                <system_message backrefs="id10" id="id9" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline interpreted text or phrase reference start-string without end-string.
                <system_message backrefs="id12" id="id11" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline emphasis start-string without end-string.
                <system_message backrefs="id14" id="id13" level="2" line="1" source="test data" type="WARNING">
                    <paragraph>
                        Inline literal start-string without end-string.
                <paragraph>
                    Definition \n\
                    <problematic id="id16" refid="id15">
                        `
                    with \n\
                    <problematic id="id18" refid="id17">
                        *
                    inline \n\
                    <problematic id="id20" refid="id19">
                        ``
                    text \n\
                    <problematic id="id22" refid="id21">
                        **
                    markup errors.
                <system_message backrefs="id16" id="id15" level="2" line="2" source="test data" type="WARNING">
                    <paragraph>
                        Inline interpreted text or phrase reference start-string without end-string.
                <system_message backrefs="id18" id="id17" level="2" line="2" source="test data" type="WARNING">
                    <paragraph>
                        Inline emphasis start-string without end-string.
                <system_message backrefs="id20" id="id19" level="2" line="2" source="test data" type="WARNING">
                    <paragraph>
                        Inline literal start-string without end-string.
                <system_message backrefs="id22" id="id21" level="2" line="2" source="test data" type="WARNING">
                    <paragraph>
                        Inline strong start-string without end-string.
"""],
]

if __name__ == '__main__':
    import unittest
    unittest.main(defaultTest='suite')
