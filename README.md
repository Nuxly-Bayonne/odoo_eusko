![License](https://img.shields.io/badge/license-LGPL--3.0-blue.svg)
![Odoo Version](https://img.shields.io/badge/Odoo-16%20%7C%2017%20%7C%2018-brightgreen)


Devise Eusko
=============

Ce module intégre la devise **Eusko (Eus)** dans Odoo pour les sociétés utilisant l'euro (€) comme devise principale.

À propos de la monnaie Eusko
----------------------------

L’Eusko est la monnaie locale complémentaire circulant au Pays Basque Nord, sur le territoire de la Communauté d'agglomération Pays Basque.

Elle vise à :
   - Relocaliser l'économie et soutenir l'emploi local
   - Accélérer la transition écologique et développer les circuits courts
   - Faire vivre la langue basque
   - Soutenir le milieu associatif

C'est la plus importante monnaie locale d'Europe, avec des milliers de particuliers et des centaines d'entreprises qui l'utilisent quotidiennement en complément de l'euro (€).

Plus d'informations : https://euskalmoneta.org

À propos Nuxly Bayonne
----------------------------
Nuxly Bayonne accompagne les entreprises du Pays basque dans la simplification de la gestion de leur entreprise. Devis, commandes, factures .. nous divisons par 2 la charge administrative avec le déploiement du logiciel Odoo.

Nos clients sont des PME, startups et associations qui veulent un partenaire de confiance pour piloter leur projet numérique, avec efficacité, proximité et bon sens.
   
Fonctionnalités
----------------
- Création automatique de la devise Eusko (code `Eus`)
- Taux de conversion initial : 1 EUR = 1 Eus
- Vérifie que la devise de la société est l'euro avant installation
- Désactive la devise lors de la désinstallation du module

Conditions
----------
- Ce module **ne peut être installé que** si la devise principale de la société est l’euro (€)

Public concerné
---------------
- Structures du Pays basque (PME, associations, etc.) adhérente à l'eusko et souhaitant suivre leurs transactions eusko, en activant l'application dans leur Odoo ou en changeant de logiciel pour passer sur Odoo.
- Structures du Pays basque pas encore adhérente à l'eusko et souhaitant déployer un logiciel de gestion prenant en charge l'eusko.
 

Installation
---------------

1. Copier ce module dans votre dossier `addons`
2. Mettre à jour la liste des modules
3. Installer le module "Odoo Eusko"

Utilisation
---------------

Une fois le module activé, vous pouvez enregistrer vos paiements en Eusko.

Roadmap
---------------

-Gestion des rapprochements bancaires

-Création des fichiers de prélèvements

Développement & Support
------------------------

### Authors
-  Développé par : **Nuxly Bayonne** 
-  Site web : https://www.nuxly.com/integrateur-odoo-bayonne/ 
-  Contact : contact@nuxly.com

### Contributors 
-  Thibaut Camberlin – tcamberlin@nuxly.com
-  Kahina Alitouche – kalitouche@nuxly.com

Bug Tracker
-----------

Les bugs sont suivis sur GitHub Issues.  
En cas de souci, consultez la liste des tickets existants.  
Si vous êtes le premier à l’identifier, aidez-nous à le corriger 
en nous transmettant un rapport clair, reproductible et précis.

https://github.com/Nuxly-Bayonne/odoo_eusko/issues

Compatibilité
-------------

- Odoo 16: branche 16.0
- Odoo 17: branche 17.0
- Odoo 18: branche 18.0