from typing import List, Optional

from backend.core.graphml.src.GraphML.GraphMLElement import GraphMLElement
from backend.core.graphml.src.GraphML.graph.common.Desc import Desc

from backend.core.graphml.src.GraphML.graph.common.ID import ID, IDType
from backend.core.graphml.src.GraphML.graph.common.NMTOKEN import NMTOKEN
from backend.core.graphml.src.GraphML.graph.elements.data.Data import Data
from backend.core.graphml.src.GraphML.graph.elements.port.Port import Port


class Edge(GraphMLElement):
    """
    Representa un elemento `<edge>` en un grafo de GraphML.
    <!ELEMENT edge (desc?,data*,graph?)>
    <!ATTLIST edge
              id         ID           #IMPLIED
              source     IDREF        #REQUIRED
              sourceport NMTOKEN      #IMPLIED
              target     IDREF        #REQUIRED
              targetport NMTOKEN      #IMPLIED
              directed   (true|false) #IMPLIED
    >
    """

    def __init__(
            self,
            source: ID,
            target: ID,
            edge_id: ID = None,
            source_port: Port = None,
            target_port: Port = None,
            directed: Optional[bool] = None,
            desc: Optional[Desc] = None,
            data_elements: Optional[List[Data]] = None,
            subgraph: Optional["Graph"] = None,  # Anotación diferida para evitar problemas circulares
    ):
        """
        Inicializa una arista.

        Args:
            source (ID): Nodo origen de la arista.
            target (ID): Nodo destino de la arista.
            edge_id (Optional[ID]): Identificador único para la arista.
            source_port (Optional[Port]): Puerto de origen de la arista.
            target_port (Optional[Port]): Puerto de destino de la arista.
            directed (Optional[bool]): Indica si la arista es dirigida (por defecto, sigue la configuración del grafo).
            desc (Optional[Desc]): Descripción opcional de la arista.
            data_elements (Optional[List[Data]]): Elementos `<data>` asociados a la arista.
            subgraph (Optional[Graph]): Subgrafo opcional contenido en la arista.
        """
        super().__init__(desc)
        self.edge_id = edge_id if edge_id else ID.autogenerate(IDType.EDGE)
        self.source = source
        self.target = target
        self.__source_port = None
        self.source_port = source_port
        self.__target_port = None
        self.target_port = target_port
        self.directed = directed
        self.data_elements = data_elements if data_elements else []
        self.subgraph = subgraph

    @property
    def source_port(self) -> Optional[str]:
        """
        Obtiene el puerto del punto final.

        Returns:
            Optional[str]: Puerto del punto final.
        """
        return self.__source_port

    @NMTOKEN
    @source_port.setter
    def source_port(self, port: Optional[str]) -> None:
        """
        Establece el puerto del punto final.

        Args:
            port (Optional[str]): Puerto del punto final.
        """
        self.__source_port = port

    @property
    def target_port(self) -> Optional[str]:
        """
        Obtiene el puerto del punto final.

        Returns:
            Optional[str]: Puerto del punto final.
        """
        return self.__target_port

    @NMTOKEN
    @target_port.setter
    def target_port(self, port: Optional[str]) -> None:
        """
        Establece el puerto del punto final.

        Args:
            port (Optional[str]): Puerto del punto final.
        """
        self.__target_port = port

    def add_data(self, data: Data) -> None:
        """
        Agrega un elemento `<data>` a la arista.

        Args:
            data (Data): Elemento de datos a agregar.
        """
        self.data_elements.append(data)

    def set_subgraph(self, subgraph: "Graph") -> None:
        """
        Establece un subgrafo en la arista.

        Args:
            subgraph (Graph): Subgrafo a asociar con la arista.
        """
        self.subgraph = subgraph

    def to_xml(self) -> str:
        """
        Convierte la arista a su representación XML.

        Returns:
            str: Representación XML de la arista.
        """
        desc_xml = f"<desc>{self.desc}</desc>" if self.desc else ""
        attributes = f'id="{self.edge_id}" source="{self.source}" target="{self.target}"'
        if self.source_port:
            attributes += f' sourceport="{self.source_port}"'
        if self.target_port:
            attributes += f' targetport="{self.target_port}"'
        if self.directed is not None:
            attributes += f' directed="{str(self.directed).lower()}"'
        data_xml = "".join(data.to_xml() for data in self.data_elements)
        subgraph_xml = self.subgraph.to_xml() if self.subgraph else ""

        # return f"<edge {attributes}>{desc_xml}{data_xml}{subgraph_xml}</edge>"
        return f"<edge {attributes}" + (">" if desc_xml or data_xml or subgraph_xml else "/>") + (
            f"{desc_xml}{data_xml}{subgraph_xml}" + f"</edge>" if desc_xml or data_xml or subgraph_xml else "")
