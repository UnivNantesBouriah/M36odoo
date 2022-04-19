# -*- coding: utf-8 -*-

from odoo import models, fields, api



class classe(models.Model):
    _name = "gestion_alternants.classe"
    _description = "gestion_alternants.classe"

    name = fields.Char(string="Classe", required = True)
    alternant_ids = fields.One2many('gestion_alternants.alternant', 'classe_id',string='Alternant')
    description = fields.Text('Intitulé de la classe')

class alternant(models.Model):
    _name = "gestion_alternants.alternant"
    _description = "gestion_alternants.alternant"

    name = fields.Char(string="Nom", required = True)
    firstname = fields.Char(string = "Prénom", required = True)
    email = fields.Char(string="email",required = True)
    classe_id = fields.Many2one('gestion_alternants.classe', string='Classe',required = True)
    entreprise_id = fields.Many2one('gestion_alternants.entreprise', string='Entreprise')
    tuteuruniv_id = fields.Many2one('gestion_alternants.tuteuruniv', string='Tuteur Université')
    tuteurent_id = fields.Many2one('gestion_alternants.tuteurent', string='Tuteur Entreprise')
    
class TuteurUniv(models.Model):
    _name = "gestion_alternants.tuteuruniv"
    _description = "gestion_alternants.tuteuruniv"

    name = fields.Char(string="Nom du tuteur", required = True)
    firstname = fields.Char(string="Prénom du tuteur", required = True)
    alternant_ids = fields.One2many('gestion_alternants.alternant', 'tuteuruniv_id',string='Alternant')
    description = fields.Text("""Description du tuteur""")
    
    def name_get(self):
        tuteurList=[]
        for tuteur in self:
            tuteurList.append((tuteur.id,'%s %s'%(tuteur.firstname ,tuteur.name)))
        return tuteurList

        
class entreprise(models.Model):
    _name = "gestion_alternants.entreprise"
    _description = "gestion_alternants.entreprise"

    name = fields.Char(string="Nom de l'entreprise", required = True)
    adresse = fields.Char(string="Adresse de l'entreprise", required = True)
    alternant_ids = fields.One2many('gestion_alternants.alternant', 'entreprise_id',string='Alternant')
    tuteurent_ids = fields.One2many('gestion_alternants.tuteurent', 'entreprise_id',string='Tuteur')
    description = fields.Text("""Description de l'entreprise""")


class TuteurEntreprise(models.Model):
    _name = "gestion_alternants.tuteurent"
    _description = "gestion_alternants.tuteurent"

    name = fields.Char(string="Nom du tuteur", required = True)
    firstname = fields.Char(string="Prénom du tuteur", required = True)
    alternant_ids = fields.One2many('gestion_alternants.alternant', 'tuteurent_id',string='Alternant')
    entreprise_id = fields.Many2one('gestion_alternants.entreprise', string='Entreprise')
    description = fields.Text("""Description de l'entreprise""")

    def name_get(self):
        tuteurList=[]
        for tuteur in self:
            tuteurList.append((tuteur.id,'%s %s'%(tuteur.firstname ,tuteur.name)))
        return tuteurList

class rdv(models.Model):
    _name = "gestion_alternants.rdv"
    _description = "gestion_alternants.rdv"
#    _rec_name = 'alternant_id'

    date = fields.Datetime(string="Date", required = True)
    type = fields.Selection([('1','1'),
                             ('2','2'),
                             ('3','3')] , string="Numéro de la rencontre", required = True)
    etat = fields.Selection([('PREVUE','Prévue'),
                              ('ANNULEE','Annulée'),
                              ('FAITE','Faite')
                              ])
    alternant_id = fields.Many2one('gestion_alternants.alternant', string='Alternant')   
    entreprise_ref = fields.Many2one(related='alternant_id.entreprise_id', string='Entreprise')
    tuteurent_ref = fields.Many2one(related='alternant_id.tuteurent_id', string='Tuteur Entreprise')
    tuteuruniv_ref = fields.Many2one(related='alternant_id.tuteuruniv_id', string='Tuteur Universitaire')
    description = fields.Text("""Description de la rencontre""")
    
    def name_get(self):
        alternantList=[]
        for rencontre in self:
            alternantList.append((rencontre.id,'%s %s %s'%(rencontre.entreprise_ref.name,rencontre.alternant_id.firstname ,rencontre.alternant_id.name)))
        return alternantList
    
    def rdv_send_mail(self):
        print("Send email")
        template_id = self.env.ref('gestion_alternants.mail_template_rdv').id
        self.env['mail.template'].browse(template_id).send_mail(self.id,force_send=True)


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
