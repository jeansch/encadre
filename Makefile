top: README.html routes.html

%.html: %.org
	cat _org/header >$@
	cat _org/style.css >>$@
	cat _org/body >>$@
	cat $< | ./_org/org2html.js >> $@
	cat _org/footer >>$@


routes.org: encadre_test_controllers/*.py
	encadre-test-app-dump-routes config.ini >routes.org

tests:
	nosetests --nocapture --with-coverage --cover-inclusive --cover-package=encadre,encadre_flask,encadre_test_controllers,encadre_test_app
