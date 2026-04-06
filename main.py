from dbblog import creer_table, ajouter_article , lire_articles

# créer la table (une seule fois au lancement)
creer_table()

# ajouter un article (test)
# ajouter_article("Mon test", "Hello ImmyBloom ✨")

# lire les articles
articles = lire_articles()

for article in articles:
    print(article)