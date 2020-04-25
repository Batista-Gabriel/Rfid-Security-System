const db = require('../connection')

module.exports={
    async create(req,res){
        const {card_id}= req.body
        await db
        .insert({card_id})
        .into('card');
        res.json({sucess:true})
    },

    async index(req,res){
        await db
        .select()
        .from('card')
        .then(function(data){
            res.send(data);
        });
    },

    async card(req,res){
        console.log(req.params.id)
        await db
        .select()
        .from('card')
        .where({card_id:req.params.id})
        .then(function(data){
            res.send(data)
        })
    },

    async cardUser(req,res){
        await db
        .select()
        .from('user')
        .innerJoin('card','card_id_fk','card_id')
        .where({card_id:req.params.id})
        .then(function(data){
            res.send(data)
        })        
    },


    async delete(req,res){
        await db
        .del()
        .where({card_id:req.params.id})
        .from('card');
        res.json({sucess:true})
    }
}