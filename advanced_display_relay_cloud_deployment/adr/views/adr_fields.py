import sys
sys.path.append("/var/www/adr")
import json
from flask import Blueprint, render_template, request, url_for, redirect
from models.adr_fields import adr_Field

adr_field_blueprint = Blueprint('adr_fields', __name__)

# base page
@adr_field_blueprint.route('/', methods=['GET', 'POST'])
def doc_adr_field():
    #print("MADE IT INTO FUNCTION")
    return '{"message" : "adr string field object database management"}'

# C for Create
@adr_field_blueprint.route('/new', methods=['GET', 'POST'])
def create_adr_field():
    if request.method == 'GET':
        adr_field = request.args['adr_field']
        cf_in_mongo = False
        try:
            adr_f = adr_Field.get_by_field(adr_field)
            cf_in_mongo = True
        except:
            cf_in_mongo = False
        if cf_in_mongo == False:
            adr_field = request.args['adr_field']
            json_data = request.args['json_data']
            adr_Field(adr_field, json_data).save_to_mongo()
        if cf_in_mongo == True:
            adr_field_to_update = request.args['adr_field']
            adr_field = adr_Field.get_by_field(adr_field_to_update)
            original_adr_field = adr_Field.get_by_id(adr_field._id)
            original_adr_field.json_data = request.args.get('json_data')
            original_adr_field.save_to_mongo()

    return '{"message" : "adr string object added to database"}'

# R for Read
@adr_field_blueprint.route('/read')
def get_by_adr_field():
    adr_field = request.args['adr_field']
    adr_field = adr_Field.get_by_field(adr_field)
    return adr_field.json()

# R for internal Read
@adr_field_blueprint.route('/read_internal/<adr_field>')
def read_internal(adr_field):
    adr_field = adr_Field.get_by_field(adr_field)
    return adr_field.json()

# U for Update
@adr_field_blueprint.route('/update')
def update_adr_field():
    adr_field_to_update = request.args['adr_field']
    adr_field = adr_Field.get_by_field(adr_field_to_update)
    original_adr_field = adr_Field.get_by_id(adr_field._id)
    original_adr_field.json_data = request.args.get('json_data')
    original_adr_field.save_to_mongo()
    return '{"message" : "adr string object updated in database"}'

# D for Delete
@adr_field_blueprint.route('/delete')
def delete_adr_field():
    adr_field_to_delete = request.args['adr_field']
    adr_field = adr_Field.get_by_field(adr_field_to_delete)
    adr_field.get_by_id(adr_field._id).remove_from_mongo()
    return '{"message" : "adr_field removed from database"}'
