DABUZZ_DIR = /dabuzz
DABUZZ_SERVER = stonelinks.org
DABUZZ_USER = rcos-dabuzz
LOCAL_PORT=5001

deploy.remote:
	@rsync -ahvve ssh --delete --exclude-from=.rsync-ignore ./ $(DABUZZ_USER)@$(DABUZZ_SERVER):$(DABUZZ_DIR)/server
	@ssh $(DABUZZ_USER)@$(DABUZZ_SERVER) 'cd $(DABUZZ_DIR)/server && \
	                                      $(MAKE) echo.deployed '

echo.deployed:
	@echo "\n"
	@echo "======================================"
	@echo "=   server deployed to remote!       ="
	@echo "======================================"
	@echo "\n\n"

run.local:
	@python server.py $(LOCAL_PORT)
