import os
from typing import List

# Esta função usa a SDK oficial OpenAI (nova interface) quando disponível.

OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def _format_reviews(reviews: List[str]) -> str:

    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY is not set')
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = (
            "Você é um assistente que resume reclamações de clientes de restaurantes."
            "Receba as avaliações abaixo e retorne um parágrafo objetivo com os principais problemas e sentimentos."
            f"\n\nAvaliações:\n{_format_reviews(reviews)}\n\nResumo:"
        )

        resp = client.chat.completions.create(
            model = OPENAI_MODEL,
            messages = [{"role": "user", "content": prompt}],
            max_tokens = 300
        )

        choices = resp.get('choices') if isinstance(resp, dict) else getattr(resp, 'choices', None)
        if choices:
            content = choices[0].get('message', {}).get('content') if isinstance(choices[0], dict) else None
            if content:
                return content.strip()
        
        raise RuntimeError('LLm não retornou um sumario valido')
    
    except Exception as e:
        raise

def llm_generate_recommendations(summary: str) -> List[str]:
    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY is not set')
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = (
            "Você é um consultor de operações de restaurantes. Com base no resumo abaixo, liste 5 ações práticas, curtas e ordenadas por prioridade (máx 6 palavras cada)."
            f"\n\nResumo:\n{summary}\n\nAções:"
        )

        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        choices = resp.get('choices') if isinstance(resp, dict) else getattr(resp, 'choices', None)
        if choices:
            content = choices[0].get('message', {}).get('content') if isinstance(choices[0], dict) else None
            if content:
                lines = [l.strip('-• ').strip() for l in content.splitlines() if l.strip()]
                return lines[:5]
                
            raise RuntimeError('LLM did not return valid recommendations')
    except Exception as e:
            raise

def llm_generate_summary(reviews: List[str]) -> str:
    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY is not set')
    
    from openai import OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = (
        "Resuma de forma clara e objetiva as principais reclamações dos clientes listadas abaixo. "
        "Foque em problemas de atendimento, qualidade da comida, tempo de espera e outras dores operacionais. "
        "Faça um único parágrafo com as principais conclusões.\n\n"
        "Avaliações:\n"
        + "\n".join(f"- {r}" for r in reviews)
        + "\n\nResumo:"
    )

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.4
    )

    return response.choices[0].message.content.strip()



