top: README.html routes.html

%.html: %.org
	cat _org/header >$@
	cat _org/style.css >>$@
	cat _org/body >>$@
	cat $< | ./_org/org2html.js >> $@
	cat _org/footer >>$@


routes.org: cadre_test_controllers/*.py
	cadre-test-app-dump-routes config.ini >routes.org

tests:
	nosetests --nocapture --with-coverage --cover-inclusive --cover-package=cadre,cadre_flask,cadre_test_controllers,cadre_test_app
