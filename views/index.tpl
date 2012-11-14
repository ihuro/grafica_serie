%include header extra_css=extra_css

    <div class="container">

        <h1>Graficar</h1>

        <form class="form-horizontal span5" action="" method="POST">
            <fieldset>
                <div class="control-group">
                    <label class="control-label" for="serie">Ingrese la serie</label>
                    <div class="controls">
                        <div class="input-append">
                        <input type="text" class="span4" id="serie" name="serie" placeholder="1,2,3,4" />
                        <p class="help-block">La serie deben ser n&uacute;meros separados por coma, por ejemplo: 1,2,3,4 </p>
                        </div>
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="xlabel">Label para Eje X/Y</label>
                    <div class="controls">
                        <div class="input-append">
                        <input type="text" class="span2" id="xlabel" name="xlabel" placeholder="Eje X" />
                        </div>
                        <div class="input-append">
                        <input type="text" class="span2" id="ylabel" name="ylabel" placeholder="Eje Y" />
                        </div>
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="power">Potencia/Tiempo</label>
                    <div class="controls">
                        <div class="input-append">
                        <input type="text" class="span2" id="power" name="power" placeholder="2" />
                        </div>
                    </div>
                </div>
                <div class="control-group">
                    <label class="control-label" for="titulo">T&iacute;tulo del gr&aacute;fico</label>
                    <div class="controls">
                        <div class="input-append">
                          <input type="text" class="span2" id="titulo" name="titulo" placeholder="Título" />
                        </div>
                    </div>
                </div>
                <span class="btn btn-primary offset4" id="btnVer" value="Ver">Ver</span>
            </fieldset>
        </form>

      <div id="imagen" class="span5 offset1"></div>

    </div> <!-- /container -->

%include footer extra_js=extra_js
