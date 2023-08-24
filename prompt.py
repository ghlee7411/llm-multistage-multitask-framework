DOCUMENT_RERANKING_PROMPT_TEMPLATE = """\
Given a question and a set of documents, please read the documents and rerank them. You can select up to 3 documents.
Please list the documents in order of priority, with the highest priority document first.
Question and documents are provided below with triple quotes for clarity. Please do not include the triple quotes in your response.

'''Question
{question}
'''

'''Documents
{documents}
'''

Reranked documents:
"""

DOCUMENT_SUMMARIZATION_PROMPT_TEMPLATE = """\
Given a question and a set of documents, please read the documents and summarize them.
Question and documents are provided below with triple quotes for clarity. Please do not include the triple quotes in your response.

'''Question
{question}
'''

'''Documents
{documents}
'''

Summary:
"""

DOCUMENT_SYNTHESIS_PROMPT_TEMPLATE = """\
Given a question and a set of documents, please read the documents and synthesize the key elements.
Question and documents are provided below with triple quotes for clarity. Please do not include the triple quotes in your response.

'''Question
{question}
'''

'''Documents
{documents}
'''

Synthesis Key Elements:
"""

ANSWER_GENERATION_PROMPT_TEMPLATE = """\
Given a question and a set of documents, please read the documents and generate an answer.
Question, documents, summary, and key elements are provided below with triple quotes for clarity. 
Please do not include the triple quotes in your response.


'''Question
{question}
'''

'''Documents
{documents}
'''

'''Summary
{summary}
'''

'''Key Elements
{key_elements}
'''

Answer:
"""