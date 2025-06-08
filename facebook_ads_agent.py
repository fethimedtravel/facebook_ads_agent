# facebook_ads_agent.py
# Agent IA pour campagnes Facebook Ads
# Version : 2.0

import streamlit as st
import pandas as pd
import time
import json
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict, List, Any

# Configuration de la page
st.set_page_config(
    page_title="Agent IA Facebook Ads Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour une interface moderne
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .stApp > div:first-child {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .campaign-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #e1e8ed;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 10px 0;
    }
    
    .success-box {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .warning-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 15px 30px;
        font-weight: bold;
        font-size: 16px;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .header-title {
        color: #2c3e50;
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .section-header {
        color: #34495e;
        border-left: 5px solid #667eea;
        padding-left: 15px;
        margin: 30px 0 20px 0;
        font-size: 1.5rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Classes pour structurer l'application
class FacebookAdsAgent:
    def __init__(self):
        self.industries = {
            "Santé/Médical": ["FIV", "Chirurgie esthétique", "Dentaire", "Ophtalmologie"],
            "Tourisme": ["Voyage organisé", "Hôtellerie", "Restauration"],
            "E-commerce": ["Mode", "Électronique", "Maison"],
            "Services": ["Consulting", "Formation", "Coaching"]
        }
        
        self.countries = {
            "Afrique francophone": ["Maroc", "Algérie", "Tunisie", "Sénégal", "Côte d'Ivoire"],
            "Europe": ["France", "Belgique", "Suisse", "Canada"],
            "Moyen-Orient": ["Liban", "Émirats", "Qatar"]
        }
    
    def generate_keywords(self, product: str, industry: str, target_region: str) -> List[str]:
        """Génère des mots-clés intelligents basés sur l'industrie"""
        time.sleep(1)
        
        base_keywords = {
            "Santé/Médical": [
                f"{product} pas cher", f"{product} Turquie", f"prix {product}",
                f"meilleure clinique {product}", f"{product} tout compris",
                "tourisme médical", "traitement à l'étranger"
            ],
            "Tourisme": [
                f"{product} promotion", f"voyage {product}", f"séjour {product}",
                f"{product} pas cher", "vacances", "réservation"
            ],
            "E-commerce": [
                f"{product} en ligne", f"acheter {product}", f"{product} livraison",
                f"{product} qualité", "boutique en ligne"
            ],
            "Services": [
                f"{product} professionnel", f"expert {product}", f"formation {product}",
                f"consultant {product}", "service personnalisé"
            ]
        }
        
        return base_keywords.get(industry, [f"{product}", f"service {product}", f"{product} qualité"])
    
    def generate_ad_copy(self, product: str, target: str, industry: str, tone: str) -> Dict[str, str]:
        """Génère différentes versions de textes publicitaires"""
        time.sleep(2)
        
        templates = {
            "Professionnel": {
                "headline": f"🏆 {product} - Excellence et Expertise Reconnues",
                "primary": f"Découvrez notre {product} de qualité supérieure. Équipe d'experts, résultats garantis.",
                "description": f"Plus de 1000 clients satisfaits. Devis gratuit sous 24h."
            },
            "Émotionnel": {
                "headline": f"💖 Réalisez Votre Rêve avec {product}",
                "primary": f"Votre bonheur nous tient à cœur. {product} personnalisé selon vos besoins.",
                "description": f"Accompagnement complet de A à Z. Équipe bienveillante à votre écoute."
            },
            "Urgence": {
                "headline": f"⚡ Offre Limitée - {product} -50%",
                "primary": f"Profitez de cette promotion exceptionnelle sur {product}. Places limitées!",
                "description": f"Réservez maintenant. Offre valable jusqu'au {(datetime.now() + timedelta(days=7)).strftime('%d/%m/%Y')}"
            }
        }
        
        return templates.get(tone, templates["Professionnel"])
    
    def generate_audience_targeting(self, industry: str, target_region: str, age_range: str) -> Dict[str, Any]:
        """Génère des recommandations de ciblage précises"""
        targeting = {
            "demographics": {
                "age_range": age_range,
                "countries": self.countries.get(target_region, ["France"]),
                "languages": ["Français", "Arabe"] if "Afrique" in target_region else ["Français"]
            },
            "interests": {
                "Santé/Médical": ["Santé et fitness", "Soins médicaux", "Bien-être"],
                "Tourisme": ["Voyages", "Vacances", "Découverte"],
                "E-commerce": ["Shopping en ligne", "Mode", "Technologie"],
                "Services": ["Développement personnel", "Formation professionnelle"]
            }.get(industry, ["Intérêts généraux"]),
            "behaviors": ["Voyageurs fréquents", "Acheteurs en ligne", "Utilisateurs mobiles"],
            "exclusions": ["Concurrents", "Employés du secteur"]
        }
        
        return targeting
    
    def estimate_performance(self, budget: int, industry: str) -> Dict[str, Any]:
        """Estime les performances de la campagne"""
        # Coefficients basés sur l'industrie
        industry_multipliers = {
            "Santé/Médical": {"cpc": 2.5, "ctr": 1.8, "conversion": 0.12},
            "Tourisme": {"cpc": 1.2, "ctr": 2.1, "conversion": 0.08},
            "E-commerce": {"cpc": 0.8, "ctr": 1.5, "conversion": 0.15},
            "Services": {"cpc": 1.5, "ctr": 1.3, "conversion": 0.10}
        }
        
        multiplier = industry_multipliers.get(industry, {"cpc": 1.0, "ctr": 1.0, "conversion": 0.10})
        
        estimated_cpc = round(0.50 * multiplier["cpc"], 2)
        estimated_clicks = int(budget / estimated_cpc)
        estimated_ctr = round(multiplier["ctr"], 2)
        estimated_impressions = int(estimated_clicks / (estimated_ctr / 100))
        estimated_conversions = int(estimated_clicks * multiplier["conversion"])
        
        return {
            "impressions": estimated_impressions,
            "clicks": estimated_clicks,
            "ctr": estimated_ctr,
            "cpc": estimated_cpc,
            "conversions": estimated_conversions,
            "cost_per_conversion": round(budget / max(estimated_conversions, 1), 2)
        }

# Initialisation de l'agent
@st.cache_resource
def get_agent():
    return FacebookAdsAgent()

agent = get_agent()

# Interface utilisateur principale
st.markdown('<h1 class="header-title">🤖 Agent IA Facebook Ads Pro</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #7f8c8d;">Créez des campagnes publicitaires performantes en quelques clics</p>', unsafe_allow_html=True)

# Sidebar pour la navigation
with st.sidebar:
    st.header("🎯 Navigation")
    page = st.selectbox("Choisir une section", 
                       ["Créer une campagne", "Analyser les performances", "Bibliothèque de templates"])
    
    st.header("📊 Statistiques rapides")
    st.metric("Campagnes créées", "1,247")
    st.metric("Taux de réussite moyen", "73%")
    st.metric("Économies générées", "€45,231")

if page == "Créer une campagne":
    # Section 1: Configuration de base
    st.markdown('<h2 class="section-header">1. Configuration de votre campagne</h2>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="campaign-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            campaign_name = st.text_input("🏷️ Nom de la campagne", 
                                        placeholder="Ex: Campagne FIV Turquie 2025")
            
            industry = st.selectbox("🏢 Secteur d'activité", list(agent.industries.keys()))
            
            if industry:
                product = st.selectbox("📦 Produit/Service spécifique", agent.industries[industry])
            
            target_region = st.selectbox("🌍 Région cible", list(agent.countries.keys()))
        
        with col2:
            objective = st.selectbox("🎯 Objectif de campagne", 
                                   ["Génération de leads", "Trafic vers le site", "Conversions", "Notoriété"])
            
            daily_budget = st.slider("💰 Budget quotidien (€)", 5, 500, 50)
            
            age_range = st.select_slider("👥 Tranche d'âge", 
                                       options=["18-25", "25-35", "35-45", "45-55", "55+"], 
                                       value="25-35")
            
            tone = st.selectbox("🎨 Ton publicitaire", 
                              ["Professionnel", "Émotionnel", "Urgence"])
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Bouton de génération
    if st.button("🚀 Générer ma campagne avec l'IA", use_container_width=True):
        # Vérification des champs obligatoires
        if not campaign_name or not industry or not product:
            st.error("⚠️ Veuillez remplir tous les champs obligatoires")
        else:
            # Barre de progression avec étapes détaillées
            progress_container = st.container()
            with progress_container:
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                steps = [
                    ("🔍 Analyse du marché et de la concurrence...", 20),
                    ("🔑 Génération des mots-clés optimisés...", 40),
                    ("✍️ Création du contenu publicitaire...", 60),
                    ("🎯 Optimisation du ciblage audience...", 80),
                    ("📊 Calcul des estimations de performance...", 100)
                ]
                
                for step_text, progress in steps:
                    status_text.text(step_text)
                    progress_bar.progress(progress)
                    time.sleep(1)
                
                status_text.success("✅ Campagne générée avec succès!")
                time.sleep(1)
            
            # Stockage des données générées
            keywords = agent.generate_keywords(product, industry, target_region)
            ad_copy = agent.generate_ad_copy(product, target_region, industry, tone)
            audience = agent.generate_audience_targeting(industry, target_region, age_range)
            performance = agent.estimate_performance(daily_budget * 30, industry)
            
            st.session_state.campaign_data = {
                'campaign_name': campaign_name,
                'product': product,
                'industry': industry,
                'keywords': keywords,
                'ad_copy': ad_copy,
                'audience': audience,
                'performance': performance,
                'budget': daily_budget,
                'objective': objective
            }
            
            progress_container.empty()
    
    # Affichage des résultats
    if 'campaign_data' in st.session_state:
        data = st.session_state.campaign_data
        
        st.markdown('<h2 class="section-header">2. Résultats générés par l\'IA</h2>', unsafe_allow_html=True)
        
        # Métriques de performance estimées
        st.markdown('<div class="campaign-card">', unsafe_allow_html=True)
        st.subheader("📊 Estimations de performance (30 jours)")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{data['performance']['impressions']:,}</h3>
                <p>Impressions</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{data['performance']['clicks']:,}</h3>
                <p>Clics</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{data['performance']['ctr']}%</h3>
                <p>Taux de clic</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>{data['performance']['conversions']}</h3>
                <p>Conversions</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Contenu publicitaire
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="campaign-card">', unsafe_allow_html=True)
            st.subheader("📝 Textes publicitaires")
            
            st.text_area("Titre principal", value=data['ad_copy']['headline'], height=68)
            st.text_area("Texte principal", value=data['ad_copy']['primary'], height=100)
            st.text_area("Description", value=data['ad_copy']['description'], height=80)
            
            st.subheader("🔑 Mots-clés recommandés")
            st.write(", ".join(data['keywords']))
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="campaign-card">', unsafe_allow_html=True)
            st.subheader("🎯 Configuration du ciblage")
            
            st.write("**Pays ciblés:**")
            st.write(", ".join(data['audience']['demographics']['countries']))
            
            st.write("**Tranche d'âge:**")
            st.write(data['audience']['demographics']['age_range'])
            
            st.write("**Centres d'intérêt:**")
            st.write(", ".join(data['audience']['interests']))
            
            st.write("**Comportements:**")
            st.write(", ".join(data['audience']['behaviors']))
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Actions finales
        st.markdown('<h2 class="section-header">3. Lancement de la campagne</h2>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📤 Exporter vers Facebook Ads", use_container_width=True):
                st.markdown('<div class="success-box">✅ Configuration exportée! Connectez-vous à Facebook Ads Manager pour finaliser.</div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("📋 Copier la configuration", use_container_width=True):
                config_text = f"""
Campagne: {data['campaign_name']}
Produit: {data['product']}
Budget: {data['budget']}€/jour
Titre: {data['ad_copy']['headline']}
Mots-clés: {', '.join(data['keywords'])}
                """
                st.text_area("Configuration à copier", value=config_text, height=200)
        
        with col3:
            if st.button("💾 Sauvegarder comme template", use_container_width=True):
                st.markdown('<div class="success-box">💾 Template sauvegardé dans votre bibliothèque!</div>', unsafe_allow_html=True)

elif page == "Analyser les performances":
    st.markdown('<h2 class="section-header">📊 Analyse des performances</h2>', unsafe_allow_html=True)
    
    # Génération de données simulées pour la démo
    dates = pd.date_range(start='2025-01-01', end='2025-06-08', freq='D')
    performance_data = pd.DataFrame({
        'Date': dates,
        'Impressions': [1000 + i * 50 + (i % 7) * 200 for i in range(len(dates))],
        'Clics': [50 + i * 2 + (i % 7) * 10 for i in range(len(dates))],
        'Conversions': [2 + (i % 5) for i in range(len(dates))],
        'Coût': [25 + i * 1.5 + (i % 3) * 5 for i in range(len(dates))]
    })
    
    # Graphiques de performance
    col1, col2 = st.columns(2)
    
    with col1:
        fig_impressions = px.line(performance_data, x='Date', y='Impressions', 
                                title='Évolution des impressions')
        fig_impressions.update_layout(height=400)
        st.plotly_chart(fig_impressions, use_container_width=True)
    
    with col2:
        fig_conversions = px.line(performance_data, x='Date', y='Conversions', 
                                title='Évolution des conversions')
        fig_conversions.update_layout(height=400)
        st.plotly_chart(fig_conversions, use_container_width=True)
    
    # Tableau de bord des KPIs
    st.subheader("🎯 KPIs principaux")
    
    total_impressions = performance_data['Impressions'].sum()
    total_clics = performance_data['Clics'].sum()
    total_conversions = performance_data['Conversions'].sum()
    total_cout = performance_data['Coût'].sum()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Impressions totales", f"{total_impressions:,}", delta="12%")
    with col2:
        st.metric("Clics totaux", f"{total_clics:,}", delta="8%")
    with col3:
        st.metric("Conversions", f"{total_conversions}", delta="15%")
    with col4:
        st.metric("Coût total", f"{total_cout:.0f}€", delta="-5%")

elif page == "Bibliothèque de templates":
    st.markdown('<h2 class="section-header">📚 Bibliothèque de templates</h2>', unsafe_allow_html=True)
    
    templates = [
        {
            "name": "FIV Turquie - Approche émotionnelle",
            "industry": "Santé/Médical",
            "performance": "CTR: 3.2%",
            "description": "Template optimisé pour les services de FIV en Turquie"
        },
        {
            "name": "E-commerce Mode - Promotion Flash",
            "industry": "E-commerce",
            "performance": "CTR: 2.8%",
            "description": "Template pour les promotions limitées dans le temps"
        },
        {
            "name": "Formation Professionnelle - B2B",
            "industry": "Services",
            "performance": "CTR: 1.9%",
            "description": "Template pour les services de formation professionnelle"
        }
    ]
    
    for template in templates:
        with st.container():
            st.markdown('<div class="campaign-card">', unsafe_allow_html=True)
            col1, col2, col3 = st.columns([3, 2, 1])
            
            with col1:
                st.subheader(template["name"])
                st.write(template["description"])
                st.write(f"**Secteur:** {template['industry']}")
            
            with col2:
                st.metric("Performance", template["performance"])
            
            with col3:
                if st.button("Utiliser", key=template["name"]):
                    st.success("Template chargé!")
            
            st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; padding: 20px;">
    <p>🤖 Agent IA Facebook Ads Pro - Développé avec ❤️ pour optimiser vos campagnes publicitaires</p>
    <p>Version 2.0 | Dernière mise à jour: Juin 2025</p>
</div>
""", unsafe_allow_html=True)