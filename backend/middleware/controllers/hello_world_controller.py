from flask_restplus import Resource, Namespace

hello_ns = Namespace('hello', description='Hello World namespace')


@hello_ns.route('/')
class HelloWorld(Resource):
    @hello_ns.doc('hello world controller')
    def get(self):
        return {'app': 'middleware'}, 200
