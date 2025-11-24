from typing import List

def recommend_actions(summary_text: str) -> List[str]:
    s = summary_text.lower()
    recs = []
    if any(word in s for word in ['entrega', 'demor', 'tempo']):
        recs.append('Revisar parceiros de entregas e SLA; implementar alertas para pedidos atrasados')
    if any(word in s for word in ['frio', 'temperatura', 'esfriou']):
        recs.append('Melhorar isolamentos das embalagens e checar processo de embalagem')
    if any(word in s for word in ['atendimento', 'funcionári', 'rude']):
        recs.append('Treinamento de atendimento e script para resolução de reclamações')
    if not recs:
        recs = [
            'Solicitar feedback detalhado em casos negativos para identificar causas',
            'Monitorar avaliações semanalmente e priorizar problemas recorrentes'
        ]
    return recs